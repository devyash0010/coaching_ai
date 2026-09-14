import { useEffect, useState } from 'react'
import { fetchLeaderboard } from '../api/students.js'

export default function LeaderboardPage() {
  const [leaders, setLeaders] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchLeaderboard()
        setLeaders(data)
      } catch {
        setError('Unable to load leaderboard data')
      }
    }
    load()
  }, [])

  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Leaderboard</span><h1>Student Rank List</h1></div>
      </header>
      <section className="panel table-panel">
        <table className="data-table">
          <thead>
            <tr><th>Rank</th><th>Student</th><th>ID</th><th>Batch</th><th>Average Score</th></tr>
          </thead>
          <tbody>
            {leaders.map((row) => (
              <tr key={row.student_id}>
                <td>{row.rank}</td>
                <td>{row.name}</td>
                <td>{row.student_id}</td>
                <td>{row.batch}</td>
                <td>{row.average_score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </section>
  )
}
