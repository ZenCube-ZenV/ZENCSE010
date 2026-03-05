/*
 * US-21 — Auto-Verification When QR Code is Scanned
 * US-22 — LinkedIn Share Button on Verification Result
 *
 * TODO (Students):
 * 1. Read certificate ID from URL params: useParams()
 *    e.g. URL is /v/CERT-550e8400... → certificateId = "CERT-550e8400..."
 *
 * 2. On mount, automatically call GET /api/v1/verify/:certificateId
 *    (No user interaction needed — result shows immediately on QR scan)
 *
 * 3. While loading: show a spinner
 *
 * 4. On result, render based on result field:
 *
 *    "VALID" → Green card showing:
 *      - ✅ "Certificate is Authentic"
 *      - Recipient Name
 *      - Course Title
 *      - Issued Date
 *      - Issued By (institution_name)
 *      - Expiry Date (if present)
 *      - "Add to LinkedIn" button (see LinkedIn URL format below)
 *
 *    "REVOKED" → Orange card showing:
 *      - ⚠️ "This Certificate Has Been Revoked"
 *      - certificate_id
 *      - message from API
 *
 *    "TAMPERED" → Red card showing:
 *      - ❌ "Certificate Data Has Been Tampered"
 *      - message from API
 *
 *    "NOT_FOUND" → Red card showing:
 *      - ❌ "Certificate Not Found"
 *      - message from API
 *
 * 5. LinkedIn "Add to Profile" URL format:
 *    https://www.linkedin.com/profile/add
 *      ?startTask=CERTIFICATION_NAME
 *      &name=<course_title>
 *      &organizationName=<institution_name>
 *      &issueYear=<YYYY>
 *      &issueMonth=<MM>
 *      &certUrl=<current page URL>
 *      &certId=<certificate_id>
 *
 * API: GET http://localhost:8000/api/v1/verify/:certificateId
 * No authentication required.
 *
 * Expected response:
 * {
 *   "result": "VALID",
 *   "certificate_id": "CERT-550e8400...",
 *   "recipient_name": "John Doe",
 *   "course_title": "Full Stack Development",
 *   "issued_at": "2026-03-05T10:00:00Z",
 *   "expires_at": null,
 *   "institution_name": "CertShield Institution",
 *   "verified_at": "2026-03-05T14:22:00Z",
 *   "message": "Certificate is authentic and valid."
 * }
 */

import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

export default function VerificationResult() {
  const { certificateId } = useParams()
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // TODO: call GET /api/v1/verify/:certificateId
    // set result from API response
    // set loading to false when done
  }, [certificateId])

  if (loading) {
    return <div>Verifying certificate...</div>
  }

  // TODO: render result card based on result.result value
  return (
    <div>
      <h1>Verification Result</h1>
      <p>Certificate ID: {certificateId}</p>
      <p>TODO: Show VALID / REVOKED / TAMPERED / NOT_FOUND card here</p>
    </div>
  )
}
