import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom'
import DashboardPage from './pages/Dashboard.jsx'
import StudentsPage from './pages/Students.jsx'
import StudentProfilePage from './pages/StudentProfile.jsx'
import PerformancePage from './pages/Performance.jsx'
import TestsPage from './pages/Tests.jsx'
import TestDetailPage from './pages/TestDetail.jsx'
import LeaderboardPage from './pages/Leaderboard.jsx'
import StudyMaterialPage from './pages/StudyMaterial.jsx'
import AiAssistantPage from './pages/AiAssistant.jsx'
import AnalyticsPage from './pages/Analytics.jsx'
import SettingsPage from './pages/Settings.jsx'
import './styles.css'

function App() {
  return (
    <BrowserRouter>
      <div className="app-shell">
        <aside className="sidebar">
          <div className="brand">
            <span className="brand-mark">C</span>
            <span className="brand-text">Coaching AI</span>
          </div>
          <nav className="nav">
            <NavLink className="nav-link" end to="/">Dashboard</NavLink>
            <NavLink className="nav-link" to="/students">Students</NavLink>
            <NavLink className="nav-link" to="/students/JEE001">Student Profile</NavLink>
            <NavLink className="nav-link" to="/performance">Performance</NavLink>
            <NavLink className="nav-link" to="/tests">Tests</NavLink>
            <NavLink className="nav-link" to="/tests/T001">Test Detail</NavLink>
            <NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink>
            <NavLink className="nav-link" to="/study-material">Study Material</NavLink>
            <NavLink className="nav-link" to="/ai-assistant">AI Assistant</NavLink>
            <NavLink className="nav-link" to="/analytics">Analytics</NavLink>
            <NavLink className="nav-link" to="/settings">Settings</NavLink>
          </nav>
        </aside>

        <main className="main">
          <section className="topbar">
            <div>
              <span className="crumb">Coaching AI /</span>
              <span className="page-title">Teacher Workspace</span>
            </div>
            <div className="top-actions">
              <input className="search" placeholder="Search students" />
              <button className="icon-button">N</button>
              <button className="profile-button">Teacher</button>
            </div>
          </section>

          <Routes>
            <Route path="/" element={<DashboardPage />} />
            <Route path="/students" element={<StudentsPage />} />
            <Route path="/students/:studentId" element={<StudentProfilePage />} />
            <Route path="/performance" element={<PerformancePage />} />
            <Route path="/tests" element={<TestsPage />} />
            <Route path="/tests/:testId" element={<TestDetailPage />} />
            <Route path="/leaderboard" element={<LeaderboardPage />} />
            <Route path="/study-material" element={<StudyMaterialPage />} />
            <Route path="/ai-assistant" element={<AiAssistantPage />} />
            <Route path="/analytics" element={<AnalyticsPage />} />
            <Route path="/settings" element={<SettingsPage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
