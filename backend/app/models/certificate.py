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

class Recipient(BaseModel):
    name: str
    email: EmailStr
    student_id: Optional[str] = None


class CertificateInfo(BaseModel):
    title: str
    description: str
    skills: List[str] = []


class Signature(BaseModel):
    algorithm: str
    key_id: str
    value: str
    data_hash: str


class QR(BaseModel):
    url: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class Certificate(BaseModel):
    certificate_id: str = Field(default_factory=lambda: f"CERT-{uuid4()}")
    recipient: Recipient
    certificate: CertificateInfo
    issued_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None

    signature: Signature
    qr: QR

    status: str = "ACTIVE"
    verification_count: int = 0
    last_verified_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
