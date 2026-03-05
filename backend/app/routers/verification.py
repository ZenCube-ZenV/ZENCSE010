"""
Public verification endpoint — called when someone scans a QR code.
No authentication required. Rate-limited to 60 requests/minute per IP.

TODO (Students):
  Implement:

  GET /api/v1/verify/{certificate_id}
    - Extract client IP from Request object
    - Call verification_service.verify_certificate(certificate_id, client_ip)
    - Return VerificationResult (always HTTP 200)
    - Apply rate limit decorator from slowapi

  Hint:
    from slowapi import Limiter
    from slowapi.util import get_remote_address

    limiter = Limiter(key_func=get_remote_address)

    @router.get("/{certificate_id}")
    @limiter.limit("60/minute")
    async def verify(certificate_id: str, request: Request):
        ...
"""

# TODO: implement verification router here
