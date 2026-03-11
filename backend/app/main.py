"""
FastAPI application entry point.

TODO (Students):
  Wire everything together:

  1. Create FastAPI app with title, description, version
  2. Add lifespan handler:
       - On startup: call database.create_indexes()
       - On shutdown: call database.close_connection()
  3. Add CORS middleware (allow all origins for dev)
  4. Register slowapi rate limiter on the app
  5. Register exception handlers from exceptions/handlers.py
  6. Include routers:
       - certificates.router
       - verification.router
       - admin.router

  Hint:
    from contextlib import asynccontextmanager
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from app import database
    from app.routers import certificates, verification, admin

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await database.create_indexes()
        yield
        await database.close_connection()

    app = FastAPI(title="CertShield API", version="1.0.0", lifespan=lifespan)
"""

# TODO: implement main.py here
import pymongo
from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient

# Make sure you configure your MongoDB connection string appropriately
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "certshield"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Application Startup ---
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]
    
    # 1. Unique index on certificate_id
    await db.certificates.create_index("certificate_id", unique=True)
    
    # 2. Unique index on signature.data_hash
    await db.certificates.create_index("signature.data_hash", unique=True)
    
    # 3. Index on recipient.email
    await db.certificates.create_index("recipient.email")
    
    # 4. Compound index on status + expires_at
    await db.certificates.create_index([("status", pymongo.ASCENDING), ("expires_at", pymongo.ASCENDING)])
    
    # 5. Indexes on verification_logs.certificate_id and verified_at
    await db.verification_logs.create_index("certificate_id")
    await db.verification_logs.create_index("verified_at")
    
    # Optional: Attach db to app instance for request handlers to use
    app.state.db = db
    
    yield
    
    # --- Application Shutdown ---
    client.close()

# Pass the lifespan context to FastAPI
app = FastAPI(lifespan=lifespan)
