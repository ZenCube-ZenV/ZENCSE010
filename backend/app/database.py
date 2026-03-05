from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.config import settings

# Module-level client — created once, reused across all requests
_client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    """Return the shared Motor client (created on first call)."""
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.mongodb_url)
    return _client


def get_database() -> AsyncIOMotorDatabase:
    """Return the certshield database handle."""
    return get_client()[settings.mongodb_db_name]


# Convenience accessors for each collection
def get_certificates_collection():
    return get_database()["certificates"]


def get_verification_logs_collection():
    return get_database()["verification_logs"]


async def create_indexes() -> None:
    """
    Create all MongoDB indexes at startup.
    Called once from main.py lifespan handler.
    """
    certs = get_certificates_collection()

    await certs.create_index("certificate_id", unique=True, name="idx_certificate_id")
    await certs.create_index("recipient.email", name="idx_recipient_email")
    await certs.create_index(
        [("status", 1), ("expires_at", 1)], name="idx_status_expiry"
    )
    await certs.create_index(
        "signature.data_hash", unique=True, name="idx_data_hash"
    )

    logs = get_verification_logs_collection()
    await logs.create_index("certificate_id", name="idx_log_cert_id")
    await logs.create_index("verified_at", name="idx_log_verified_at")


async def close_connection() -> None:
    """Close the MongoDB connection. Called from main.py lifespan shutdown."""
    global _client
    if _client is not None:
        _client.close()
        _client = None
