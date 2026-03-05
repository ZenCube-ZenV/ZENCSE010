"""
Rate Limiter Configuration using slowapi.

TODO (Students):
  Configure and export a shared Limiter instance used by the verification router.

  Steps:
  1. Create a Limiter using get_remote_address as the key function
     (this limits by client IP address)

  2. Export the limiter so it can be:
     a. Registered on the FastAPI app in main.py
     b. Used as a decorator in routers/verification.py

  3. In main.py, attach the limiter to the app:
       app.state.limiter = limiter
       app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

  4. In routers/verification.py, apply the limit:
       @limiter.limit("60/minute")
       async def verify(request: Request, certificate_id: str): ...

  Hint:
    from slowapi import Limiter, _rate_limit_exceeded_handler
    from slowapi.util import get_remote_address
    from slowapi.errors import RateLimitExceeded

    limiter = Limiter(key_func=get_remote_address)

  Note: The Request object must be the first parameter in any rate-limited
  route handler for slowapi to extract the client IP correctly.
"""

# TODO: implement rate limiter here
