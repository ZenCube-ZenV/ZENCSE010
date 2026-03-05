"""
Global exception handlers for FastAPI.

TODO (Students):
  Register the following handlers on the FastAPI app (in main.py):

  1. certificate_not_found_handler
     - Catches CertificateNotFoundException
     - Returns HTTP 404 JSON: { "error": "Certificate not found", "certificate_id": "..." }

  2. validation_error_handler
     - Catches RequestValidationError (Pydantic)
     - Returns HTTP 422 JSON: { "error": "Validation failed", "details": [...] }

  3. generic_error_handler
     - Catches Exception (catch-all)
     - Returns HTTP 500 JSON: { "error": "Internal server error" }
     - Log the full traceback

  Also define:
  class CertificateNotFoundException(Exception):
      def __init__(self, certificate_id: str):
          self.certificate_id = certificate_id

  Hint:
    from fastapi import Request
    from fastapi.responses import JSONResponse

    async def certificate_not_found_handler(request: Request, exc: CertificateNotFoundException):
        return JSONResponse(status_code=404, content={...})
"""

# TODO: implement exception classes and handlers here
