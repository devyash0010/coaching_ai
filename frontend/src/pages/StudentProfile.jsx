import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { fetchStudents, fetchResults } from '../api/students.js'

export default function StudentProfilePage() {
  const { studentId } = useParams()
  const [student, setStudent] = useState(null)
  const [results, setResults] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function load() {
      try {
        setLoading(true)
        const [students, resultRows] = await Promise.all([
          fetchStudents(),
          fetchResults(),
        ])
        const match = students.find((row) => row.student_id === studentId)
        setStudent(match || null)
        setResults(resultRows.filter((row) => row.student_id === studentId))
      } catch {
        setError('Unable to load student profile')
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [studentId])

  if (loading) return <section className="page-wrap"><div className="skeleton">Loading profile…</div></section>
  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>
  if (!student) return <section className="page-wrap"><div className="empty-box">Student not found</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Student Profile</span><h1>{student.name}</h1></div>
      </header>
      <section className="profile-grid">
        <article className="panel profile-card">
          <div className="profile-summary">
            <span className="profile-avatar">{student.name.split(' ').map((n) => n[0]).slice(0, 2).join('')}</span>
            <div>
              <div className="profile-id">{student.student_id}</div>
              <div className="profile-batch">{student.batch}</div>
            </div>
          </div>
          <div className="profile-stats">
            <div><span className="stat-label">Attendance</span><span className="stat-value">{student.attendance}%</span></div>
            <div><span className="stat-label">Latest Rank</span><span className="stat-value">{results[0]?.rank ?? '—'}</span></div>
          </div>
        </article>
        <article className="panel">
          <div className="panel-header">
            <div><span className="panel-label">Assessment History</span><h3>Results</h3></div>
          </div>
          <div className="list">
            {results.map((row) => (
              <div className="list-row" key={`${row.student_id}-${row.test_id}`}>
                <span className="list-key">{row.test_id}</span>
                <span className="list-meta">Total {row.total} · Rank {row.rank}</span>
              </div>
            ))}
          </div>
        </article>
      </section>
    </section>
  )
}
