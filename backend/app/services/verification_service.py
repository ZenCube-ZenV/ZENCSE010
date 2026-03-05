"""
Verification Service — validates a certificate when QR is scanned.

TODO (Students):
  Implement one async function:

  verify_certificate(certificate_id: str, client_ip: str) -> VerificationResult
    Steps:
      1. Look up certificate_id in the certificates collection
      2. If not found → return VerificationResult(result="NOT_FOUND", ...)
      3. If status == "REVOKED" → return VerificationResult(result="REVOKED", ...)
      4. Re-build the same data dict that was originally signed
         (same fields, same order as in certificate_service.issue_certificate)
      5. Call signature_service.verify_certificate(data, stored_signature)
      6. If False → return VerificationResult(result="TAMPERED", ...)
      7. If True → increment verification_count and set last_verified_at in DB
      8. Log the event to verification_logs collection
      9. Return VerificationResult(result="VALID", ...)

  Important: Steps 2, 3, 4, 5, 6 must all return identical HTTP 200 responses
  with different result values. Never return 404 for a missing certificate —
  this prevents attackers from knowing which IDs exist.
"""

# TODO: implement verification_service here
