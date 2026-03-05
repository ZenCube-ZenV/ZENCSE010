/*
 * US-20 — Manual Certificate ID Verification Page
 *
 * TODO (Students):
 * 1. Render a centered page with:
 *    - CertShield logo / heading
 *    - A text input labeled "Enter Certificate ID"
 *    - A "Verify" button
 *
 * 2. On submit:
 *    - Show a loading spinner
 *    - Call GET /api/v1/verify/:certificateId (NO auth header — public endpoint)
 *    - Navigate to /v/:certificateId OR render VerificationResult inline
 *
 * 3. Works on mobile browsers (responsive layout)
 *
 * API: GET http://localhost:8000/api/v1/verify/:certificateId
 * No authentication required.
 *
 * Hint:
 *   import { useNavigate } from 'react-router-dom'
 *   const navigate = useNavigate()
 *   navigate(`/v/${certificateId}`)
 */

import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function VerifyPage() {
  const [certificateId, setCertificateId] = useState('')
  const navigate = useNavigate()

  // TODO: implement VerifyPage component
  return (
    <div>
      <h1>Verify Certificate</h1>
      <p>TODO: Build the manual verification form here</p>
      <input
        type="text"
        placeholder="Enter Certificate ID (e.g. CERT-550e8400...)"
        value={certificateId}
        onChange={(e) => setCertificateId(e.target.value)}
      />
      <button onClick={() => navigate(`/v/${certificateId}`)}>
        Verify
      </button>
    </div>
  )
}
