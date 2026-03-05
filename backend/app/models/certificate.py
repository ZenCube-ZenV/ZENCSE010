"""
MongoDB document model for a Certificate.

TODO (Students):
  Define the Certificate document structure using Pydantic.
  Fields to include:
    - certificate_id: str  (UUID4 prefixed with "CERT-")
    - recipient: dict      (name, email, student_id)
    - certificate: dict    (title, description, skills list)
    - issued_at: datetime
    - expires_at: datetime | None
    - signature: dict      (algorithm, key_id, value, data_hash)
    - qr: dict             (url, generated_at)
    - status: str          ("ACTIVE" | "REVOKED" | "EXPIRED")
    - verification_count: int
    - last_verified_at: datetime | None
    - created_at: datetime

  Hint: Use Pydantic BaseModel with Field defaults.
        MongoDB _id can be handled as PyObjectId or ignored (use certificate_id as primary key).
"""

# TODO: implement Certificate model here
