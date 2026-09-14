import { useState } from 'react'
import { askAssistant } from '../api/ai.js'

export default function AiAssistantPage() {
  const [question, setQuestion] = useState('Which students are weak in Physics?')
  const [answer, setAnswer] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function runQuestion() {
    setError('')
    setLoading(true)
    try {
      const data = await askAssistant(question)
      setAnswer(data.answer)
    } catch (err) {
      setError('Unable to load AI recommendation')
    } finally {
      setLoading(false)
    }
  }

  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">AI Assistant</span><h1>Coaching Intelligence</h1></div>
      </header>
      <section className="ai-layout">
        <article className="panel ai-panel">
          <div className="panel-header"><div><span className="panel-label">Ask the assistant</span><h3>Question</h3></div></div>
          <textarea className="ai-input" value={question} onChange={(e) => setQuestion(e.target.value)}></textarea>
          <div className="ai-actions">
            <button className="primary-button" onClick={runQuestion} disabled={loading}>{loading ? 'Thinking...' : 'Ask'}</button>
            <button className="panel-button" onClick={() => setAnswer('')}>Clear</button>
          </div>
          {error && <div className="error-box">{error}</div>}
        </article>
        <article className="panel ai-panel">
          <div className="panel-header"><div><span className="panel-label">Answer</span><h3>Grounded response</h3></div></div>
          <div className="answer-box">{answer || 'No answer yet'}</div>
        </article>
      </section>
    </section>
  )
}
