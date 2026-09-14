import { useEffect, useState } from 'react'
import { fetchDashboard, fetchStudents, fetchLeaderboard } from '../api/students.js'

export default function DashboardPage() {
  const [dashboard, setDashboard] = useState(null)
  const [students, setStudents] = useState([])
  const [leaderboard, setLeaderboard] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function load() {
      try {
        setLoading(true)
        const [dashResult, studentsResult, leaderResult] = await Promise.allSettled([
          fetchDashboard(),
          fetchStudents(),
          fetchLeaderboard(),
        ])

        const failures = []
        if (dashResult.status === 'fulfilled') {
          setDashboard(dashResult.value)
        } else {
          failures.push(`dashboard: ${dashResult.reason?.message || 'Failed to fetch dashboard'}`)
        }

        if (studentsResult.status === 'fulfilled') {
          setStudents(studentsResult.value)
        } else {
          failures.push(`students: ${studentsResult.reason?.message || 'Failed to fetch students'}`)
        }

        if (leaderResult.status === 'fulfilled') {
          setLeaderboard(leaderResult.value)
        } else {
          failures.push(`leaderboard: ${leaderResult.reason?.message || 'Failed to fetch leaderboard'}`)
        }

        if (failures.length > 0) {
          setError(`Unable to load dashboard data: ${failures.join(' | ')}`)
        }
      } catch (err) {
        setError(`Unable to load dashboard data: ${err?.message || 'Unknown dashboard fetch error'}`)
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [])

  if (loading) return <section className="page-wrap"><div className="skeleton">Loading dashboard…</div></section>
  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head">
        <div>
          <span className="kicker">Good morning</span>
          <h1>Coaching Analytics</h1>
        </div>
        <button className="primary-button">Generate Insight</button>
      </header>

      {error && <div className="error-box">{error}</div>}

      <section className="kpi-grid">
        <article className="kpi-card">
          <div className="kpi-top"><span className="kpi-label">Total Students</span><span className="kpi-icon">S</span></div>
          <div className="kpi-value">{dashboard?.total_students ?? '—'}</div>
          <div className="kpi-detail">Active learners</div>
        </article>
        <article className="kpi-card">
          <div className="kpi-top"><span className="kpi-label">Average Score</span><span className="kpi-icon">A</span></div>
          <div className="kpi-value">{dashboard?.average_score ?? '—'}</div>
          <div className="kpi-detail">Leaderboard average</div>
        </article>
        <article className="kpi-card">
          <div className="kpi-top"><span className="kpi-label">Attendance</span><span className="kpi-icon">T</span></div>
          <div className="kpi-value">{dashboard?.average_attendance ?? '—'}</div>
          <div className="kpi-detail">Overall cohort</div>
        </article>
        <article className="kpi-card">
          <div className="kpi-top"><span className="kpi-label">Top Performer</span><span className="kpi-icon">R</span></div>
          <div className="kpi-value">{leaderboard[0]?.student_id ?? '—'}</div>
          <div className="kpi-detail">{leaderboard[0]?.name ?? 'No data'}</div>
        </article>
      </section>

      <section className="analytics-grid">
        <article className="panel panel-wide">
          <div className="panel-header">
            <div><span className="panel-label">Performance Overview</span><h3>Academic Trend</h3></div>
            <button className="panel-button">This term</button>
          </div>
          <div className="chart-placeholder"><div className="chart-bars"><span style={{ height: '30%' }}></span><span style={{ height: '40%' }}></span><span style={{ height: '50%' }}></span><span style={{ height: '45%' }}></span><span style={{ height: '65%' }}></span><span style={{ height: '60%' }}></span><span style={{ height: '74%' }}></span></div></div>
        </article>

        <article className="panel">
          <div className="panel-header">
            <div><span className="panel-label">Subject Performance</span><h3>Subject Average</h3></div>
          </div>
          <div className="subject-bars">
            <div><span className="bar-label">Physics</span><span className="bar-track"><span className="bar bar-physics" style={{ width: '72%' }}></span></span></div>
            <div><span className="bar-label">Chemistry</span><span className="bar-track"><span className="bar bar-chemistry" style={{ width: '56%' }}></span></span></div>
            <div><span className="bar-label">Maths</span><span className="bar-track"><span className="bar bar-maths" style={{ width: '68%' }}></span></span></div>
          </div>
        </article>
      </section>

      <section className="two-column">
        <article className="panel">
          <div className="panel-header"><div><span className="panel-label">Weak Areas</span><h3>Priority Topics</h3></div></div>
          <div className="list">
            <div className="list-row"><span className="list-key">Maths</span><span className="list-meta">Low confidence</span></div>
            <div className="list-row"><span className="list-key">Chemistry</span><span className="list-meta">Needs revision</span></div>
            <div className="list-row"><span className="list-key">Physics</span><span className="list-meta">Improve speed</span></div>
          </div>
        </article>

        <article className="panel">
          <div className="panel-header"><div><span className="panel-label">Top Students</span><h3>Leaderboard</h3></div></div>
          <div className="student-list">
            {students.slice(0, 5).map((s) => <div className="list-row" key={s.student_id}><span className="list-key">{s.name}</span><span className="list-meta">{s.student_id}</span></div>)}
          </div>
        </article>
      </section>
    </section>
  )
}
