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
