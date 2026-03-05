import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import IssueCertificate from './pages/IssueCertificate'
import CertificateList from './pages/CertificateList'
import CertificateDetail from './pages/CertificateDetail'

/*
 * TODO (Students):
 * - Add a Navbar/Sidebar layout component that wraps all pages
 * - Add API_KEY to localStorage or an env variable (VITE_API_KEY)
 * - Add an axios instance in src/api/client.js that attaches X-API-Key header
 */

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/issue" element={<IssueCertificate />} />
        <Route path="/certificates" element={<CertificateList />} />
        <Route path="/certificates/:id" element={<CertificateDetail />} />
      </Routes>
    </BrowserRouter>
  )
}
