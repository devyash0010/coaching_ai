import { apiGet } from './client.js'

export async function fetchAnalyticsDashboard() {
  return apiGet('/teacher/dashboard')
}

export async function fetchPerformanceOverview() {
  return apiGet('/teacher/results')
}
