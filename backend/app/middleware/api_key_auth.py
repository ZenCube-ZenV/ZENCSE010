"""
API Key Authentication dependency for FastAPI.

TODO (Students):
  Implement:

  verify_api_key(x_api_key: str = Header(...)) -> None
    - Read the X-API-Key header value
    - Compare it to settings.api_key using secrets.compare_digest()
      (use secrets.compare_digest to prevent timing attacks)
    - If mismatch → raise HTTPException(status_code=401, detail="Invalid API Key")
    - If match → return (FastAPI will allow the request through)

  Hint:
    import secrets
    from fastapi import Header, HTTPException
    from app.config import settings

    async def verify_api_key(x_api_key: str = Header(...)):
        if not secrets.compare_digest(x_api_key, settings.api_key):
            raise HTTPException(status_code=401, detail="Invalid API Key")
"""

# TODO: implement API key auth dependency here
