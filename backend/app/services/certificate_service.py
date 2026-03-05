"""
Certificate Service — business logic for issuing and managing certificates.

TODO (Students):
  Implement the following async functions:

  1. issue_certificate(request: CertificateCreateRequest) -> CertificateResponse
     Steps:
       a. Generate certificate_id = "CERT-" + str(uuid.uuid4())
       b. Build the certificate data dict (fields to sign)
       c. Call signature_service.sign_certificate(data) → (signature, data_hash)
       d. Build verification_url = f"{settings.verify_base_url}/{certificate_id}"
       e. Call qr_service.generate_qr_base64(verification_url) → qr_base64
       f. Build LinkedIn share URL (see plan for URL format)
       g. Build the full MongoDB document and insert into certificates collection
       h. Return CertificateResponse

  2. get_certificate(certificate_id: str) -> dict | None
     - Find one document by certificate_id field
     - Return None if not found

  3. list_certificates(skip: int, limit: int) -> list[dict]
     - Return paginated list from certificates collection
     - Sort by created_at descending

  4. revoke_certificate(certificate_id: str, reason: str, revoked_by: str) -> bool
     - Update status to "REVOKED"
     - Set revocation.revokedAt, revocation.reason, revocation.revokedBy
     - Return True if document was updated, False if not found

  5. get_stats() -> dict
     - Return counts: total, active, revoked, verifications_today
"""

# TODO: implement certificate_service functions here
