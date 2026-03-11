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
import uuid
import urllib.parse
from datetime import datetime, timezone
import pymongo
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient

from schemas import CertificateCreateRequest, CertificateResponse
from models import CertificateDocument, RecipientModel, CertificateDetailsModel, SignatureModel, QRCodeModel, CertificateStatus
from signature_service import sign_certificate
from qr_service import generate_qr_base64

class Settings:
    verify_base_url = "http://localhost:3000/v"
    
settings = Settings()

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.certshield

async def issue_certificate(request: CertificateCreateRequest) -> CertificateResponse:
    """Issues a new certificate, signs it, generates a QR code, and stores it in MongoDB."""
    cert_id = "CERT-" + str(uuid.uuid4())
    
    data_to_sign = {
        "recipient": {
            "name": request.recipient_name,
            "email": request.recipient_email,
            "student_id": request.recipient_student_id,
        },
        "certificate": {
            "title": request.course_title,
            "description": request.description,
            "skills": request.skills,
        },
        "issued_at": request.issue_date.isoformat(),
    }
    
    # Await async function calls
    signature_b64, data_hash = await sign_certificate(data_to_sign)
    
    verification_url = f"{settings.verify_base_url}/{cert_id}"
    
    qr_base64 = await generate_qr_base64(verification_url)
    
    base_linkedin = "https://www.linkedin.com/profile/add"
    params = {
        "startTask": "CERTIFICATE_VIEW",
        "name": request.course_title,
        "organizationId": "123456",
        "issueYear": request.issue_date.year,
        "issueMonth": request.issue_date.month,
        "certUrl": verification_url,
        "certId": cert_id
    }
    linkedin_share_url = f"{base_linkedin}?{urllib.parse.urlencode(params)}"
    
    now = datetime.now(timezone.utc)
    
    cert_doc = CertificateDocument(
        certificate_id=cert_id,
        recipient=RecipientModel(
            name=request.recipient_name,
            email=request.recipient_email,
            student_id=request.recipient_student_id or ""
        ),
        certificate=CertificateDetailsModel(
            title=request.course_title,
            description=request.description or "",
            skills=request.skills
        ),
        issued_at=now,
        expires_at=datetime.combine(request.expiry_date, datetime.min.time()).replace(tzinfo=timezone.utc) if request.expiry_date else None,
        signature=SignatureModel(
            algorithm="ECDSA-SHA256",
            key_id="primary",
            value=signature_b64,
            data_hash=data_hash
        ),
        qr=QRCodeModel(
            url=verification_url,
            generated_at=now
        ),
        status=CertificateStatus.ACTIVE,
        verification_count=0,
        last_verified_at=None,
        created_at=now
    )
    
    cert_dict = cert_doc.model_dump()
    
    await db.certificates.insert_one(cert_dict)
    
    return CertificateResponse(
        certificate_id=cert_id,
        qr_code_base64=qr_base64,
        qr_code_url=verification_url,
        linkedin_share_url=linkedin_share_url,
        issued_at=now,
        status=cert_doc.status.value
    )

async def get_certificate(certificate_id: str) -> Optional[dict]:
    """Find one document by certificate_id field. Return None if not found."""
    return await db.certificates.find_one({"certificate_id": certificate_id}, {"_id": 0})

async def list_certificates(skip: int, limit: int) -> List[dict]:
    """Return paginated list from certificates collection. Sort by created_at descending."""
    cursor = db.certificates.find({}, {"_id": 0}).sort("created_at", pymongo.DESCENDING).skip(skip).limit(limit)
    return await cursor.to_list(length=limit)

async def revoke_certificate(certificate_id: str, reason: str, revoked_by: str) -> bool:
    """Update status and revocation details. Return True if updated, False if not found."""
    result = await db.certificates.update_one(
        {"certificate_id": certificate_id},
        {
            "$set": {
                "status": "REVOKED",
                "revocation": {
                    "revokedAt": datetime.now(timezone.utc),
                    "reason": reason,
                    "revokedBy": revoked_by
                }
            }
        }
    )
    return result.modified_count > 0

async def get_stats() -> dict:
    """Return counts: total, active, revoked, verifications_today."""
    total = await db.certificates.count_documents({})
    active = await db.certificates.count_documents({"status": "ACTIVE"})
    revoked = await db.certificates.count_documents({"status": "REVOKED"})
    
    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    verifications_today = await db.verification_logs.count_documents({
        "verified_at": {"$gte": today}
    })
    
    return {
        "total": total,
        "active": active,
        "revoked": revoked,
        "verifications_today": verifications_today
    }
