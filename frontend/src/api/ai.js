import { apiPost } from './client.js'

export async function askAssistant(question) {
  return apiPost('/teacher/chat', { question })
}
