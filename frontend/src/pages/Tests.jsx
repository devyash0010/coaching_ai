import { useEffect, useState } from 'react'
import { fetchResults } from '../api/students.js'

export default function TestsPage() {
  const [results, setResults] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchResults()
        setResults(data)
      } catch {
        setError('Unable to load test data')
      }
    }
    load()
  }, [])

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Tests</span><h1>Assessment Analytics</h1></div>
      </header>
      {error && <div className="error-box">{error}</div>}
      <section className="panel table-panel">
        <table className="data-table">
          <thead>
            <tr><th>Student</th><th>Test</th><th>Physics</th><th>Chemistry</th><th>Maths</th><th>Total</th><th>Rank</th></tr>
          </thead>
          <tbody>
            {results.slice(0, 30).map((row) => (
              <tr key={`${row.student_id}-${row.test_id}`}>
                <td>{row.student_id}</td>
                <td>{row.test_id}</td>
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
