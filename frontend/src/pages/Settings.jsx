export default function SettingsPage() {
  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Settings</span><h1>Workspace Settings</h1></div>
      </header>
      <section className="panel">
        <div className="list">
          <div className="list-row"><span className="list-key">Backend URL</span><span className="list-meta">http://127.0.0.1:8000</span></div>
          <div className="list-row"><span className="list-key">Model</span><span className="list-meta">qwen2.5:3b</span></div>
          <div className="list-row"><span className="list-key">Embedding</span><span className="list-meta">all-mpnet-base-v2</span></div>
        </div>
      </section>
    </section>
  )
}
