import { useEffect, useState } from 'react'
import { fetchStudents } from '../api/students.js'

export default function StudentsPage() {
  const [students, setStudents] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function load() {
      try {
        setLoading(true)
        const data = await fetchStudents()
        setStudents(data)
      } catch (err) {
        setError('Unable to load student data')
      } finally {
        setLoading(false)
      }
    }

    load()
  }, [])

  if (loading) return <section className="page-wrap"><div className="skeleton">Loading students…</div></section>
  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div>
          <span className="kicker">Students</span>
          <h1>Student Management</h1>
        </div>
      </header>
      <section className="panel table-panel">
        <div className="panel-header">
          <div><span className="panel-label">Student Directory</span><h3>{students.length} Students</h3></div>
        </div>
        <table className="data-table">
          <thead>
            <tr><th>Student</th><th>ID</th><th>Class / Batch</th><th>Attendance</th></tr>
          </thead>
          <tbody>
            {students.map((s) => (
              <tr key={s.student_id}>
                <td>{s.name}</td>
                <td>{s.student_id}</td>
                <td>{s.batch}</td>
                <td>{s.attendance}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </section>
  )
}
