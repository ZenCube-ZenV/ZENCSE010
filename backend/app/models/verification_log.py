"""
MongoDB document model for a Verification Log entry.

TODO (Students):
  Define the VerificationLog document structure.
  Fields to include:
    - certificate_id: str      (which certificate was verified)
    - result: str              ("VALID" | "REVOKED" | "TAMPERED" | "NOT_FOUND")
    - verified_at: datetime
    - client_ip: str           (IP of the person who scanned)

  One log entry is created every time someone calls GET /api/v1/verify/{certificate_id}.
"""

# TODO: implement VerificationLog model here
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

class VerificationResult(str, Enum):
    VALID = "VALID"
    REVOKED = "REVOKED"
    TAMPERED = "TAMPERED"
    NOT_FOUND = "NOT_FOUND"

class VerificationLog(BaseModel):
    """
    MongoDB document model for a Verification Log entry.
    One log entry is created every time someone calls GET /api/v1/verify/{certificate_id}.
    """
    certificate_id: str
    result: VerificationResult
    verified_at: datetime
    client_ip: str
