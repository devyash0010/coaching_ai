import { useEffect, useState } from 'react'
import { fetchAnalyticsDashboard } from '../api/analytics.js'

export default function AnalyticsPage() {
  const [analytics, setAnalytics] = useState(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function load() {
      try {
        setLoading(true)
        const data = await fetchAnalyticsDashboard()
        setAnalytics(data)
      } catch {
        setError('Unable to load analytics')
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [])

  if (loading) return <section className="page-wrap"><div className="skeleton">Loading analytics…</div></section>
  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Analytics</span><h1>Performance Intelligence</h1></div>
      </header>
      {error && <div className="error-box">{error}</div>}
      <section className="analytics-grid">
        <article className="panel panel-wide">
          <div className="panel-header">
            <div><span className="panel-label">Cohort Health</span><h3>Attendance & Scores</h3></div>
          </div>
          <div className="chart-placeholder">
            <div className="chart-bars">
              <span style={{ height: '32%' }}></span>
              <span style={{ height: '44%' }}></span>
              <span style={{ height: '58%' }}></span>
              <span style={{ height: '60%' }}></span>
              <span style={{ height: '62%' }}></span>
              <span style={{ height: '76%' }}></span>
              <span style={{ height: '72%' }}></span>
            </div>
          </div>
        </article>
        <article className="panel">
          <div className="panel-header">
            <div><span className="panel-label">Signals</span><h3>Insights</h3></div>
          </div>
          <div className="list">
            <div className="list-row"><span className="list-key">Completion</span><span className="list-meta">84%</span></div>
            <div className="list-row"><span className="list-key">Avg. Score</span><span className="list-meta">{analytics?.average_score ?? '—'}</span></div>
            <div className="list-row"><span className="list-key">Attendance</span><span className="list-meta">{analytics?.average_attendance ?? '—'}</span></div>
          </div>
        </article>
      </section>
    </section>
  )
}
