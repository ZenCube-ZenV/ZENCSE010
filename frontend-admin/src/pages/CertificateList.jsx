/*
 * US-25 — Paginated Certificate List
 *
 * TODO (Students):
 * 1. On mount, call GET /api/v1/certificates?skip=0&limit=20 with X-API-Key header
 * 2. Render results in a table with columns:
 *    - Certificate ID
 *    - Recipient Name
 *    - Course Title
 *    - Issued Date (format: DD/MM/YYYY)
 *    - Status (colored badge: green=ACTIVE, red=REVOKED)
 *    - Actions (View button)
 *
 * 3. Add Previous / Next pagination buttons
 *    - Track current page offset in state
 *    - Disable Previous on first page, disable Next when results < limit
 *
 * 4. Clicking a row (or the View button) navigates to /certificates/:id
 *
 * API: GET http://localhost:8000/api/v1/certificates?skip=0&limit=20
 * Headers: X-API-Key: <your-api-key>
 *
 * Expected response: array of:
 * {
 *   "certificate_id": "CERT-...",
 *   "recipient_name": "John Doe",
 *   "course_title": "Full Stack Dev",
 *   "issued_at": "2026-03-05T10:00:00Z",
 *   "status": "ACTIVE"
 * }
 */

export default function CertificateList() {
  // TODO: implement CertificateList component
  return (
    <div>
      <h1>Certificates</h1>
      <p>TODO: Show paginated certificate table here</p>
    </div>
  )
}
