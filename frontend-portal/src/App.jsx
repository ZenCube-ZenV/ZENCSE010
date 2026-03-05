import { BrowserRouter, Routes, Route } from 'react-router-dom'
import VerifyPage from './pages/VerifyPage'
import VerificationResult from './pages/VerificationResult'

/*
 * TODO (Students):
 * - The portal runs on port 3001 (matches VERIFY_BASE_URL in backend .env)
 * - Route /v/:certificateId is the QR scan target — auto-verify on load
 * - Route /verify is for manual ID entry
 */

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Manual entry page */}
        <Route path="/verify" element={<VerifyPage />} />
        {/* QR scan auto-verify — certificate ID comes from the URL */}
        <Route path="/v/:certificateId" element={<VerificationResult />} />
        {/* Default redirect */}
        <Route path="*" element={<VerifyPage />} />
      </Routes>
    </BrowserRouter>
  )
}
