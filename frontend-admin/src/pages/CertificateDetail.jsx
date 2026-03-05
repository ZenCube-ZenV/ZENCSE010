/*
 * US-26 — Certificate Detail Page with Revoke Action
 *
 * TODO (Students):
 * 1. Read certificate ID from URL params: useParams()
 * 2. On mount, call GET /api/v1/certificates/:id with X-API-Key header
 * 3. Display all certificate fields:
 *    - Recipient name, email, student ID
 *    - Course title, description, skills (as tags)
 *    - Issue date, expiry date
 *    - Status badge
 *    - Verification count and last verified at
 * 4. Show QR code image: <img src={`data:image/png;base64,...`} />
 *    (Hint: call GET /api/v1/certificates/:id/qrcode to get the PNG,
 *     or render from the certificate data if you store base64)
 * 5. Add a "Download QR" button
 *
 * 6. Revoke button (only shown when status === "ACTIVE"):
 *    - Show a confirmation dialog: "Are you sure you want to revoke this certificate?"
 *    - On confirm, call PUT /api/v1/certificates/:id/revoke
 *    - On success, refresh the certificate data (status will change to REVOKED)
 *    - Hide the Revoke button after revocation
 *
 * API:
 *   GET  http://localhost:8000/api/v1/certificates/:id   (headers: X-API-Key)
 *   PUT  http://localhost:8000/api/v1/certificates/:id/revoke   (headers: X-API-Key)
 */

import { useParams } from 'react-router-dom'

export default function CertificateDetail() {
  const { id } = useParams()

  // TODO: implement CertificateDetail component
  return (
    <div>
      <h1>Certificate Detail</h1>
      <p>TODO: Show details for certificate {id}</p>
    </div>
  )
}
