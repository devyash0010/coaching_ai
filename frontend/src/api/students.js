import { apiGet } from './client.js'

export async function fetchStudents() {
  return apiGet('/teacher/students')
}

export async function fetchDashboard() {
  return apiGet('/teacher/dashboard')
}

export async function fetchResults() {
  return apiGet('/teacher/results')
}

export async function fetchLeaderboard() {
  return apiGet('/teacher/leaderboard')
}
