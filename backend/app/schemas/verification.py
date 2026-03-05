"""
Pydantic schema for the Verification API response.

TODO (Students):
  VerificationResult — returned by GET /api/v1/verify/{certificate_id}
  Fields:
    - result: str          ("VALID" | "REVOKED" | "TAMPERED" | "NOT_FOUND")
    - certificate_id: str
    - recipient_name: str | None
    - course_title: str | None
    - issued_at: datetime | None
    - expires_at: datetime | None
    - institution_name: str | None
    - verified_at: datetime         (timestamp of this verification request)
    - message: str                  (human-readable explanation)

  Example valid response:
  {
    "result": "VALID",
    "certificate_id": "CERT-550e8400...",
    "recipient_name": "John Doe",
    "course_title": "Full Stack Development",
    "issued_at": "2026-03-01T10:00:00Z",
    "expires_at": null,
    "institution_name": "CertShield Institution",
    "verified_at": "2026-03-05T14:22:00Z",
    "message": "Certificate is authentic and valid."
  }
"""

# TODO: implement VerificationResult schema here
