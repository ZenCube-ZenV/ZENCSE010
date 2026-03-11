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
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional
import uuid

from pydantic import BaseModel, Field

class CertificateStatus(str, Enum):
    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"
    EXPIRED = "EXPIRED"

class RecipientModel(BaseModel):
    name: str
    email: str
    student_id: str

class CertificateDetailsModel(BaseModel):
    title: str
    description: str
    skills: List[str]

class SignatureModel(BaseModel):
    algorithm: str
    key_id: str
    value: str
    data_hash: str

class QRCodeModel(BaseModel):
    url: str
    generated_at: datetime

def generate_certificate_id() -> str:
    """Generate a unique UUID4 prefixed with 'CERT-'."""
    return f"CERT-{uuid.uuid4()}"

class CertificateDocument(BaseModel):
    certificate_id: str = Field(
        default_factory=generate_certificate_id,
        description="Unique identifier prefixed with CERT-"
    )
    recipient: RecipientModel
    certificate: CertificateDetailsModel
    issued_at: datetime
    expires_at: Optional[datetime] = None
    signature: SignatureModel
    qr: QRCodeModel
    status: CertificateStatus
    verification_count: int = Field(default=0)
    last_verified_at: Optional[datetime] = None
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


