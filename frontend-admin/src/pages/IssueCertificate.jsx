/*
 * US-24 — Issue Certificate Form
 *
 * TODO (Students):
 * 1. Build a form with these fields:
 *    - Recipient Name (required text input)
 *    - Recipient Email (required email input)
 *    - Student ID (optional text input)
 *    - Course Title (required text input)
 *    - Description (optional textarea)
 *    - Skills (dynamic list — add/remove tags)
 *    - Issue Date (required date picker)
 *    - Expiry Date (optional date picker)
 *
 * 2. On submit, call POST /api/v1/certificates with X-API-Key header
 *    Request body:
 *    {
 *      "recipient_name": "John Doe",
 *      "recipient_email": "john@example.com",
 *      "recipient_student_id": "STU-001",
 *      "course_title": "Full Stack Development",
 *      "description": "Completed 6-month program",
 *      "skills": ["Python", "React", "MongoDB"],
 *      "issue_date": "2026-03-05",
 *      "expiry_date": null
 *    }
 *
 * 3. On success (HTTP 201):
 *    - Show the QR code image (decode qr_code_base64 and render as <img>)
 *    - Show the certificate_id
 *    - Show a "Download QR" button
 *
 * 4. On HTTP 422: show inline validation errors under each field
 * 5. On other errors: show a general error message
 *
 * Hint for rendering QR:
 *   <img src={`data:image/png;base64,${response.qr_code_base64}`} alt="QR Code" />
 *
 * Hint for Download QR button:
 *   Create a link element with href=data:image/png;base64,... and trigger click
 */

export default function IssueCertificate() {
  // TODO: implement IssueCertificate component
  return (
    <div>
      <h1>Issue Certificate</h1>
      <p>TODO: Build the certificate issuance form here</p>
    </div>
  )
}
