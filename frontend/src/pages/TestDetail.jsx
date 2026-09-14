import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { fetchResults } from '../api/students.js'

export default function TestDetailPage() {
  const { testId } = useParams()
  const [rows, setRows] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function load() {
      try {
        setLoading(true)
        const data = await fetchResults()
        setRows(data.filter((row) => row.test_id === testId))
      } catch {
        setError('Unable to load test detail')
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [testId])

  if (loading) return <section className="page-wrap"><div className="skeleton">Loading test detail…</div></section>
  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Test Detail</span><h1>{testId}</h1></div>
      </header>
      <section className="panel table-panel">
        <div className="panel-header">
          <div><span className="panel-label">Result Distribution</span><h3>{rows.length} Students</h3></div>
        </div>
        <table className="data-table">
          <thead>
            <tr><th>Student</th><th>Physics</th><th>Chemistry</th><th>Maths</th><th>Total</th><th>Rank</th></tr>
          </thead>
          <tbody>
            {rows.map((row, idx) => (
              <tr key={`${row.student_id}-${row.test_id}-${idx}`}>
                <td>{row.student_id}</td>
                <td>{row.physics}</td>
                <td>{row.chemistry}</td>
                <td>{row.maths}</td>
                <td>{row.total}</td>
                <td>{row.rank}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </section>
  )
}
