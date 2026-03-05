"""
Pydantic schemas (DTOs) for Certificate API request and response.

TODO (Students):
  1. CertificateCreateRequest — what the admin sends to POST /api/v1/certificates
     Fields:
       - recipient_name: str
       - recipient_email: str
       - recipient_student_id: str | None
       - course_title: str
       - description: str | None
       - skills: list[str]
       - issue_date: date
       - expiry_date: date | None

  2. CertificateResponse — what the API returns after issuing a certificate
     Fields:
       - certificate_id: str
       - qr_code_base64: str        (PNG image as base64 string)
       - qr_code_url: str           (verification URL embedded in QR)
       - linkedin_share_url: str
       - issued_at: datetime
       - status: str

  3. CertificateListItem — compact item for list view
     Fields: certificate_id, recipient_name, course_title, issued_at, status

  Hint: Use pydantic BaseModel. For dates use datetime.date / datetime.datetime.
"""

# TODO: implement schemas here
