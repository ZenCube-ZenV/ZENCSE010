"""
Admin REST endpoints for Certificate management.
All routes require X-API-Key header authentication.

TODO (Students):
  Implement the following FastAPI route handlers:

  POST   /api/v1/certificates          → issue_certificate()
  GET    /api/v1/certificates          → list_certificates() with ?skip=0&limit=20
  GET    /api/v1/certificates/{id}     → get_certificate()
  PUT    /api/v1/certificates/{id}/revoke → revoke_certificate()
  GET    /api/v1/certificates/{id}/qrcode → return QR PNG as image/png response

  All routes must:
    - Call verify_api_key dependency (from middleware/api_key_auth.py)
    - Call the appropriate certificate_service function
    - Return proper HTTP status codes (201 for create, 200 for others, 404 if not found)

  Hint:
    router = APIRouter(prefix="/api/v1/certificates", tags=["certificates"])

    @router.post("/", status_code=201, dependencies=[Depends(verify_api_key)])
    async def create_certificate(request: CertificateCreateRequest):
        return await certificate_service.issue_certificate(request)
"""

# TODO: implement certificate router here
