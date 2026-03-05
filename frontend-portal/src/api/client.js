/**
 * Axios instance for the Verification Portal.
 * No API key required — all verification endpoints are public.
 *
 * TODO (Students):
 * 1. Create an axios instance with:
 *    - baseURL from import.meta.env.VITE_API_URL
 *    - default Content-Type: application/json header
 *
 * 2. Add a response interceptor that:
 *    - Returns response.data directly (unwraps axios response)
 *    - On network error: returns a NOT_FOUND-like result so the UI
 *      shows a friendly error instead of crashing
 *
 * Hint:
 *   import axios from 'axios'
 *
 *   const apiClient = axios.create({
 *     baseURL: import.meta.env.VITE_API_URL,
 *     headers: { 'Content-Type': 'application/json' },
 *   })
 *
 *   export default apiClient
 *
 * Usage in components:
 *   import apiClient from '../api/client'
 *   const result = await apiClient.get(`/api/v1/verify/${certificateId}`)
 */

// TODO: implement axios client here
