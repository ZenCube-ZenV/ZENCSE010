# CertShield — Sprint Plan & User Stories
# Duration: 30 Days | 4 Sprints | 1 Week Each

---

## ROLES (Actors)
- **Admin** — Institution staff who issue and manage certificates
- **Student** — Certificate recipient who shares it
- **Verifier** — Recruiter or employer who checks authenticity
- **System** — Internal/technical stories (no human actor)

---

# SPRINT 1 — Backend Foundation
**Days 1–7 | Goal: System can issue a signed certificate with a QR code via API**

---

### EPIC: Certificate Data Modelling

---

**US-01**
**As a** System,
**I want** a MongoDB certificate document model with all required fields,
**So that** certificate data is stored in a structured, consistent format.

**Acceptance Criteria:**
- [ ] Certificate document contains: certificate_id, recipient (name, email, student_id), certificate (title, description, skills), issued_at, expires_at, signature (algorithm, key_id, value, data_hash), qr (url, generated_at), status, verification_count, last_verified_at, created_at
- [ ] certificate_id is unique (UUID4 prefixed with "CERT-")
- [ ] status field only accepts: ACTIVE, REVOKED, EXPIRED
- [ ] Model is a Pydantic BaseModel

---

**US-02**
**As a** System,
**I want** a MongoDB verification log model,
**So that** every QR scan event is recorded for audit purposes.

**Acceptance Criteria:**
- [ ] VerificationLog document contains: certificate_id, result, verified_at, client_ip
- [ ] result only accepts: VALID, REVOKED, TAMPERED, NOT_FOUND
- [ ] Model is a Pydantic BaseModel

---

**US-03**
**As a** System,
**I want** MongoDB indexes created at application startup,
**So that** certificate lookups are fast even with thousands of records.

**Acceptance Criteria:**
- [ ] Unique index on certificate_id
- [ ] Unique index on signature.data_hash
- [ ] Index on recipient.email
- [ ] Compound index on status + expires_at
- [ ] Indexes on verification_logs.certificate_id and verified_at
- [ ] Indexes are created via lifespan handler in main.py (not on every request)

---

### EPIC: Cryptographic Signing

---

**US-04**
**As a** System,
**I want** a key generation utility that creates an ECDSA P-256 key pair,
**So that** the institution has a private key for signing and a public key for verification.

**Acceptance Criteria:**
- [ ] Running `python generate_keys.py` creates private_key.pem and public_key.pem in keys/ folder
- [ ] Keys use ECDSA P-256 curve
- [ ] Keys are saved in PEM format
- [ ] keys/ folder is in .gitignore (private key never committed)

---

**US-05**
**As a** System,
**I want** a signature service that signs certificate data with ECDSA P-256,
**So that** any future tampering of certificate data can be detected.

**Acceptance Criteria:**
- [ ] sign_certificate(data: dict) returns (base64_signature: str, data_hash: str)
- [ ] Data is canonicalized (keys sorted, JSON serialized) before hashing
- [ ] SHA-256 hash is computed on the canonical data
- [ ] Signature is produced using ECDSA with SHA-256 and the private key from settings
- [ ] data_hash is returned as hex string prefixed with "sha256:"

---

**US-06**
**As a** System,
**I want** a signature verification function,
**So that** when a certificate is looked up, I can confirm it has not been tampered with.

**Acceptance Criteria:**
- [ ] verify_certificate(data: dict, signature_b64: str) returns True or False
- [ ] Uses the same canonicalization logic as sign_certificate
- [ ] Uses public key from settings
- [ ] Returns False (does not raise) if signature is invalid or malformed
- [ ] Unit test: sign then verify round-trip returns True
- [ ] Unit test: modify one field then verify returns False

---

### EPIC: QR Code Generation

---

**US-07**
**As a** System,
**I want** a QR code service that generates a PNG QR code from a verification URL,
**So that** the QR can be embedded on the certificate for easy scanning.

**Acceptance Criteria:**
- [ ] generate_qr_base64(verification_url: str) returns a base64-encoded PNG string
- [ ] QR code uses ERROR_CORRECT_M error correction level
- [ ] Output is scannable by a standard phone camera
- [ ] Unit test: generated base64 decodes to a valid PNG image

---

### EPIC: Certificate Issuance Service

---

**US-08**
**As an** Admin,
**I want** to issue a certificate by providing recipient and course details,
**So that** a cryptographically signed certificate with a QR code is created and stored.

**Acceptance Criteria:**
- [ ] issue_certificate(request) generates a unique CERT- prefixed UUID4 certificate_id
- [ ] Certificate data is signed using SignatureService
- [ ] QR code is generated pointing to: {VERIFY_BASE_URL}/{certificate_id}
- [ ] LinkedIn share URL is constructed with correct query parameters
- [ ] Full certificate document is inserted into MongoDB certificates collection
- [ ] Returns: certificate_id, qr_code_base64, qr_code_url, linkedin_share_url, issued_at, status

---

**US-09**
**As an** Admin,
**I want** to retrieve a certificate by its ID,
**So that** I can view its details from the admin dashboard.

**Acceptance Criteria:**
- [ ] get_certificate(certificate_id) returns the full document or None
- [ ] Lookup uses the indexed certificate_id field

---

**US-10**
**As an** Admin,
**I want** to list all certificates with pagination,
**So that** I can browse issued certificates from the dashboard.

**Acceptance Criteria:**
- [ ] list_certificates(skip, limit) returns a list of certificate documents
- [ ] Results are sorted by created_at descending (newest first)
- [ ] Default page size is 20

---

**US-11**
**As an** Admin,
**I want** to revoke a certificate,
**So that** a certificate that was issued by mistake or is no longer valid is flagged.

**Acceptance Criteria:**
- [ ] revoke_certificate(certificate_id, reason, revoked_by) updates status to REVOKED
- [ ] Sets revocation.revokedAt, revocation.reason, revocation.revokedBy fields
- [ ] Returns True if updated, False if certificate not found
- [ ] Revoked certificate still exists in DB (not deleted)

---

# SPRINT 2 — REST APIs + Verification Logic
**Days 8–14 | Goal: All API endpoints working end-to-end with auth and rate limiting**

---

### EPIC: Request/Response Schemas

---

**US-12**
**As a** System,
**I want** Pydantic request and response schemas for certificate operations,
**So that** all API input is validated and output is consistent.

**Acceptance Criteria:**
- [ ] CertificateCreateRequest validates: recipient_name (required), recipient_email (valid email), course_title (required), skills (list), issue_date (date), expiry_date (optional date)
- [ ] CertificateResponse contains: certificate_id, qr_code_base64, qr_code_url, linkedin_share_url, issued_at, status
- [ ] CertificateListItem contains: certificate_id, recipient_name, course_title, issued_at, status
- [ ] VerificationResult contains: result, certificate_id, recipient_name, course_title, issued_at, expires_at, institution_name, verified_at, message

---

### EPIC: Admin REST Endpoints

---

**US-13**
**As an** Admin,
**I want** a REST endpoint to issue a certificate via HTTP POST,
**So that** my institution's certificate generation system can call it programmatically.

**Acceptance Criteria:**
- [ ] POST /api/v1/certificates returns HTTP 201 with CertificateResponse
- [ ] Requires X-API-Key header (returns 401 if missing or wrong)
- [ ] Returns HTTP 422 with field errors if request body is invalid
- [ ] QR code PNG is included as base64 in the response

---

**US-14**
**As an** Admin,
**I want** REST endpoints to list, get, and revoke certificates,
**So that** I can manage the full lifecycle of certificates via API.

**Acceptance Criteria:**
- [ ] GET /api/v1/certificates returns paginated list (HTTP 200), requires API key
- [ ] GET /api/v1/certificates/{id} returns certificate detail (HTTP 200) or 404, requires API key
- [ ] PUT /api/v1/certificates/{id}/revoke returns HTTP 200 or 404, requires API key
- [ ] GET /api/v1/certificates/{id}/qrcode returns image/png binary response, requires API key

---

**US-15**
**As an** Admin,
**I want** a stats endpoint that returns certificate counts,
**So that** the admin dashboard can show a summary.

**Acceptance Criteria:**
- [ ] GET /api/v1/stats returns: { total, active, revoked, verifications_today }
- [ ] Requires API key
- [ ] verifications_today counts verification_logs entries from today (UTC)

---

### EPIC: API Key Authentication

---

**US-16**
**As a** System,
**I want** all admin endpoints protected with API key authentication,
**So that** only authorized systems can issue or manage certificates.

**Acceptance Criteria:**
- [ ] X-API-Key header is required on all admin routes
- [ ] Key comparison uses secrets.compare_digest (timing-attack safe)
- [ ] Missing header returns HTTP 401: { "error": "Invalid API Key" }
- [ ] Wrong key returns HTTP 401 (same message — no hint about why)
- [ ] Public verification endpoint requires NO authentication

---

### EPIC: Public Verification

---

**US-17**
**As a** Verifier,
**I want** to verify a certificate by scanning its QR code,
**So that** I can instantly confirm whether the certificate is authentic.

**Acceptance Criteria:**
- [ ] GET /api/v1/verify/{certificate_id} always returns HTTP 200 (never 404)
- [ ] Returns result: VALID when certificate exists, is ACTIVE, and signature verifies
- [ ] Returns result: REVOKED when certificate has been revoked
- [ ] Returns result: TAMPERED when certificate exists but signature fails
- [ ] Returns result: NOT_FOUND when certificate_id does not exist in DB
- [ ] Response includes: recipient_name, course_title, issued_at, institution_name, message
- [ ] Rate limited to 60 requests per minute per IP

---

**US-18**
**As a** System,
**I want** every verification attempt logged in the database,
**So that** the institution has an audit trail of who verified what and when.

**Acceptance Criteria:**
- [ ] A VerificationLog document is inserted on every verification call
- [ ] Log includes: certificate_id, result, verified_at (UTC), client_ip
- [ ] Logging does not block or slow down the verification response
- [ ] Logs are stored in a separate verification_logs collection

---

### EPIC: Error Handling

---

**US-19**
**As a** System,
**I want** consistent, structured error responses for all failure scenarios,
**So that** clients receive predictable JSON error payloads.

**Acceptance Criteria:**
- [ ] CertificateNotFoundException → HTTP 404: { "error": "Certificate not found", "certificate_id": "..." }
- [ ] Pydantic RequestValidationError → HTTP 422: { "error": "Validation failed", "details": [...] }
- [ ] Unhandled Exception → HTTP 500: { "error": "Internal server error" }
- [ ] 500 errors are logged with full traceback (not exposed in response)
- [ ] All errors return Content-Type: application/json

---

# SPRINT 3 — Frontend
**Days 15–21 | Goal: Verification portal and admin dashboard are functional**

---

### EPIC: Public Verification Portal (React)

---

**US-20**
**As a** Verifier,
**I want** a public web page where I can enter a certificate ID to verify it,
**So that** I don't need to scan a QR code — I can manually check any certificate.

**Acceptance Criteria:**
- [ ] Page has a text input for Certificate ID and a Verify button
- [ ] On submit, calls GET /api/v1/verify/{certificate_id}
- [ ] Shows loading spinner during API call
- [ ] Shows green VALID card with certificate details on success
- [ ] Shows red INVALID / orange REVOKED card on failure
- [ ] Works on mobile browsers

---

**US-21**
**As a** Verifier,
**I want** the verification page to open automatically when I scan the QR code,
**So that** I can verify a certificate with one scan — no typing required.

**Acceptance Criteria:**
- [ ] Route /v/{certificate_id} auto-calls the verify API with the ID from the URL
- [ ] Result is displayed immediately without any user interaction
- [ ] Page title shows: "Certificate Verification — CertShield"
- [ ] Open Graph meta tags are set so LinkedIn/WhatsApp show a rich preview

---

**US-22**
**As a** Student,
**I want** a LinkedIn share button on the verification result page,
**So that** I can add my certificate directly to my LinkedIn profile.

**Acceptance Criteria:**
- [ ] "Add to LinkedIn" button appears on VALID result cards
- [ ] Button opens LinkedIn Add-to-Profile URL in a new tab
- [ ] URL is pre-filled with: certificate title, institution name, issue year/month, cert URL, cert ID
- [ ] Button is not shown for REVOKED or INVALID certificates

---

### EPIC: Admin Dashboard (React)

---

**US-23**
**As an** Admin,
**I want** a dashboard home page showing certificate statistics,
**So that** I can see an overview of all issued certificates at a glance.

**Acceptance Criteria:**
- [ ] Dashboard shows 4 stat cards: Total Issued, Active, Revoked, Verifications Today
- [ ] Stats are fetched from GET /api/v1/stats
- [ ] Page refreshes stats every 30 seconds automatically
- [ ] Requires API key (stored in localStorage or env)

---

**US-24**
**As an** Admin,
**I want** a form to issue a new certificate,
**So that** I can create and download a certificate's QR code from the dashboard.

**Acceptance Criteria:**
- [ ] Form fields: Recipient Name, Recipient Email, Student ID (optional), Course Title, Description (optional), Skills (multi-input), Issue Date, Expiry Date (optional)
- [ ] On submit, calls POST /api/v1/certificates with X-API-Key header
- [ ] On success, shows the QR code image and a Download QR button
- [ ] Shows validation errors inline under each field on HTTP 422
- [ ] Shows success message with certificate ID

---

**US-25**
**As an** Admin,
**I want** a paginated table of all issued certificates,
**So that** I can browse, search, and manage certificates.

**Acceptance Criteria:**
- [ ] Table columns: Certificate ID, Recipient Name, Course, Issued Date, Status, Actions
- [ ] Status shown as colored badge (green = ACTIVE, red = REVOKED)
- [ ] Clicking a row opens the certificate detail page
- [ ] Pagination controls (Previous / Next) work correctly
- [ ] Page size is 20 per page

---

**US-26**
**As an** Admin,
**I want** a certificate detail page with a revoke button,
**So that** I can view full certificate details and revoke it if needed.

**Acceptance Criteria:**
- [ ] Shows all certificate fields: recipient, course, skills, dates, status, verification count
- [ ] Shows QR code image with a Download button
- [ ] Revoke button with confirmation dialog ("Are you sure you want to revoke this certificate?")
- [ ] On revoke, calls PUT /api/v1/certificates/{id}/revoke and refreshes the page
- [ ] Revoke button is hidden if certificate is already REVOKED

---

# SPRINT 4 — Docker, Testing & Deploy
**Days 22–30 | Goal: Production-ready, tested, containerized, documented**

---

### EPIC: Containerization

---

**US-27**
**As a** System,
**I want** the backend containerized with a multi-stage Dockerfile,
**So that** the app can be deployed consistently on any server.

**Acceptance Criteria:**
- [ ] Dockerfile uses python:3.12-slim base image
- [ ] All dependencies installed from requirements.txt
- [ ] App runs on port 8000 inside container
- [ ] Image size is under 300MB

---

**US-28**
**As a** Developer,
**I want** a docker-compose file that starts MongoDB and the backend together,
**So that** the full stack can be started with a single command: `docker-compose up`.

**Acceptance Criteria:**
- [ ] `docker-compose up` starts: MongoDB 7.0, CertShield backend
- [ ] Backend waits for MongoDB to be ready (depends_on)
- [ ] MongoDB data is persisted in a named volume (not lost on restart)
- [ ] keys/ folder is mounted as a volume so keys survive container restarts
- [ ] .env file is loaded from backend/.env

---

### EPIC: Testing

---

**US-29**
**As a** Developer,
**I want** unit tests for the signature service,
**So that** I can confirm the signing and verification logic is correct before deployment.

**Acceptance Criteria:**
- [ ] Test: sign then verify round-trip returns True
- [ ] Test: sign data, modify one field, verify returns False
- [ ] Test: verify with wrong public key returns False
- [ ] Tests run with `pytest` and pass without a running MongoDB

---

**US-30**
**As a** Developer,
**I want** unit tests for the QR code service,
**So that** I confirm QR codes are correctly generated.

**Acceptance Criteria:**
- [ ] Test: generate_qr_base64 returns a valid base64 string
- [ ] Test: decoded base64 is a valid PNG image
- [ ] Test: QR decodes back to the original URL

---

**US-31**
**As a** Developer,
**I want** integration tests for the certificate issuance and verification API flow,
**So that** I can confirm the full end-to-end path works correctly.

**Acceptance Criteria:**
- [ ] Test: POST /api/v1/certificates returns 201 with qr_code_base64 and certificate_id
- [ ] Test: GET /api/v1/verify/{id} returns VALID for a freshly issued certificate
- [ ] Test: PUT /api/v1/certificates/{id}/revoke, then GET /api/v1/verify/{id} returns REVOKED
- [ ] Test: GET /api/v1/verify/non-existent-id returns NOT_FOUND (HTTP 200)
- [ ] Test: POST /api/v1/certificates without X-API-Key returns 401
- [ ] Tests use an in-memory or test MongoDB instance (mongomock or testcontainers)

---

### EPIC: Security Hardening

---

**US-32**
**As a** System,
**I want** CORS configured correctly for both admin and public endpoints,
**So that** only authorized origins can call admin APIs.

**Acceptance Criteria:**
- [ ] Public verification endpoint allows requests from any origin
- [ ] Admin endpoints restrict CORS to configured allowed origins
- [ ] Preflight OPTIONS requests are handled correctly

---

**US-33**
**As a** System,
**I want** the rate limiter active on the public verification endpoint,
**So that** automated brute-force attacks are blocked.

**Acceptance Criteria:**
- [ ] GET /api/v1/verify/{id} is limited to 60 requests per minute per IP
- [ ] Exceeding the limit returns HTTP 429 with a Retry-After header
- [ ] Rate limit does not apply to admin endpoints

---

### EPIC: Documentation & Polish

---

**US-34**
**As a** Developer,
**I want** FastAPI's auto-generated OpenAPI docs to be accurate and complete,
**So that** any team integrating with the API has a clear reference.

**Acceptance Criteria:**
- [ ] /docs (Swagger UI) is available and shows all endpoints
- [ ] All request and response schemas are documented
- [ ] Authentication requirement is noted on admin endpoints
- [ ] Example request/response values are provided

---

**US-35**
**As a** Developer,
**I want** a clear README with setup and run instructions,
**So that** any new team member can get the system running in under 10 minutes.

**Acceptance Criteria:**
- [ ] README covers: Prerequisites, Clone, Setup .env, Generate keys, Install dependencies, Run locally, Run with Docker
- [ ] Key generation command is documented
- [ ] Example API call (curl) for issuing a certificate is included
- [ ] Example API call (curl) for verifying a certificate is included

---

# SUMMARY

| Sprint | Days | Stories | Goal |
|--------|------|---------|------|
| Sprint 1 | 1–7 | US-01 → US-11 | Backend core: models, signing, QR, issuance service |
| Sprint 2 | 8–14 | US-12 → US-19 | REST APIs, auth, rate limiting, verification, error handling |
| Sprint 3 | 15–21 | US-20 → US-26 | React verification portal + admin dashboard |
| Sprint 4 | 22–30 | US-27 → US-35 | Docker, tests, security, docs, deploy |
| **Total** | **30 days** | **35 stories** | **Production-ready microservice** |

---

# STORY POINT REFERENCE

| Size | Points | Example |
|------|--------|---------|
| XS | 1 | Write a Pydantic model |
| S | 2 | Write a simple service function |
| M | 3 | Write a router with 2–3 endpoints |
| L | 5 | Full service with DB + crypto logic |
| XL | 8 | Full React page with API integration |
