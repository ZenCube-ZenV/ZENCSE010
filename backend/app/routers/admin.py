"""
Admin dashboard stats endpoint.
Requires X-API-Key authentication.

TODO (Students):
  Implement:

  GET /api/v1/stats
    - Call certificate_service.get_stats()
    - Return: { total, active, revoked, verifications_today }

  Hint:
    router = APIRouter(prefix="/api/v1", tags=["admin"])

    @router.get("/stats", dependencies=[Depends(verify_api_key)])
    async def get_stats():
        return await certificate_service.get_stats()
"""

# TODO: implement admin router here
