export default function StudyMaterialPage() {
  return (
    <section className="page-wrap">
      <header className="page-head compact">
        <div><span className="kicker">Study Material</span><h1>Learning Library</h1></div>
      </header>
      <section className="panel table-panel">
        <div className="list">
          <div className="list-row"><span className="list-key">Physics Practice Set</span><span className="list-meta">Subject: Physics / Topic: Mechanics</span></div>
          <div className="list-row"><span className="list-key">Chemistry Revision Kit</span><span className="list-meta">Subject: Chemistry / Topic: Organic Chemistry</span></div>
          <div className="list-row"><span className="list-key">Maths Problem Sheet</span><span className="list-meta">Subject: Maths / Topic: Calculus</span></div>
        </div>
      </section>
    </section>
  )
}
