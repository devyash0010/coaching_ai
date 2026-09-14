const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export async function apiGet(path) {
  try {
    const response = await fetch(`${API_BASE}${path}`)
    if (!response.ok) {
      throw new Error(`API request failed: ${path} (${response.status} ${response.statusText})`)
    }
    return response.json()
  } catch (err) {
    throw new Error(err?.message || `API request failed: ${path}`)
  }
}

export async function apiPost(path, body) {
  try {
    const response = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    })
    if (!response.ok) {
      throw new Error(`API request failed: ${path} (${response.status} ${response.statusText})`)
    }
    return response.json()
  } catch (err) {
    throw new Error(err?.message || `API request failed: ${path}`)
  }
}
