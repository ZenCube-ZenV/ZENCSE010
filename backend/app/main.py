"""
FastAPI application entry point.

TODO (Students):
  Wire everything together:

  1. Create FastAPI app with title, description, version
  2. Add lifespan handler:
       - On startup: call database.create_indexes()
       - On shutdown: call database.close_connection()
  3. Add CORS middleware (allow all origins for dev)
  4. Register slowapi rate limiter on the app
  5. Register exception handlers from exceptions/handlers.py
  6. Include routers:
       - certificates.router
       - verification.router
       - admin.router

  Hint:
    from contextlib import asynccontextmanager
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from app import database
    from app.routers import certificates, verification, admin

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await database.create_indexes()
        yield
        await database.close_connection()

    app = FastAPI(title="CertShield API", version="1.0.0", lifespan=lifespan)
"""

# TODO: implement main.py here
