/*
 * US-23 — Admin Dashboard Stats Page
 *
 * TODO (Students):
 * 1. On component mount, call GET /api/v1/stats with X-API-Key header
 * 2. Display 4 stat cards:
 *    - Total Issued
 *    - Active
 *    - Revoked
 *    - Verifications Today
 * 3. Auto-refresh every 30 seconds (use setInterval + clearInterval in useEffect)
 * 4. Show a loading spinner while fetching
 * 5. Show error message if API call fails
 *
 * API: GET http://localhost:8000/api/v1/stats
 * Headers: X-API-Key: <your-api-key>
 *
 * Expected response:
 * {
 *   "total": 42,
 *   "active": 38,
 *   "revoked": 4,
 *   "verifications_today": 12
 * }
 */

export default function Dashboard() {
  // TODO: implement Dashboard component
  return (
    <div>
      <h1>Dashboard</h1>
      <p>TODO: Show certificate stats here</p>
    </div>
  )
}
