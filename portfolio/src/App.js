import React from "react";
import { ProjectsProvider } from "./context/ProjectsContext";
import ProjectList from "./components/ProjectList";
import ProjectFilter from "./components/ProjectFilter";
import "./App.css";

function App() {
  return (
    <ProjectsProvider>
      <div className="app">
        <header className="app-header">
          <h1>My Portfolio</h1>
        </header>
        <main className="app-main">
          <ProjectFilter />
          <ProjectList />
        </main>
      </div>
    </ProjectsProvider>
  );
}

export default App;
