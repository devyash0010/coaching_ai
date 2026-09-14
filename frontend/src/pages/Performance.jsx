import { useEffect, useState } from 'react'
import { fetchResults } from '../api/students.js'

export default function PerformancePage() {
  const [results, setResults] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchResults()
        setResults(data)
      } catch {
        setError('Unable to load performance data')
      }
    }
    load()
  }, [])

  if (error) return <section className="page-wrap"><div className="error-box">{error}</div></section>

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Performance</span><h1>Subject Analytics</h1></div>
      </header>
      <section className="analytics-grid">
        <article className="panel panel-wide">
          <div className="panel-header"><div><span className="panel-label">Performance Overview</span><h3>Mark Trends</h3></div></div>
          <div className="chart-placeholder"><div className="chart-bars"><span style={{ height: '35%' }}></span><span style={{ height: '45%' }}></span><span style={{ height: '56%' }}></span><span style={{ height: '44%' }}></span><span style={{ height: '74%' }}></span><span style={{ height: '66%' }}></span><span style={{ height: '78%' }}></span></div></div>
        </article>
        <article className="panel">
          <div className="panel-header"><div><span className="panel-label">Subject Comparison</span><h3>Average Scores</h3></div></div>
          <div className="subject-bars">
            <div><span className="bar-label">Physics</span><span className="bar-track"><span className="bar bar-physics" style={{ width: '66%' }}></span></span></div>
            <div><span className="bar-label">Chemistry</span><span className="bar-track"><span className="bar bar-chemistry" style={{ width: '58%' }}></span></span></div>
            <div><span className="bar-label">Maths</span><span className="bar-track"><span className="bar bar-maths" style={{ width: '70%' }}></span></span></div>
          </div>
        </article>
      </section>
    </section>
  )
}
