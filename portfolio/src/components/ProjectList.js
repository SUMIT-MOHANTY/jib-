import React from "react";
import { useProjects } from "../context/ProjectsContext";
import ProjectCard from "./ProjectCard";
import "./ProjectList.css";

const ProjectList = () => {
  const { projects, loading, error, selectedCategory } = useProjects();

  if (loading) return <div className="loading">Loading projects...</div>;
  if (error) return <div className="error">Error: {error}</div>;
  if (!projects.length) return <div className="empty">No projects found in category: {selectedCategory}</div>;

  return (
    <div className="project-list">
      {projects.map(project => (
        <ProjectCard key={project.id} project={project} />
      ))}
    </div>
  );
};

export default ProjectList;
