import React from "react";
import { useProjects } from "../context/ProjectsContext";
import "./ProjectFilter.css";

const ProjectFilter = () => {
  const { categories, selectedCategory, setSelectedCategory } = useProjects();

  const allCategories = ["all", ...categories];

  return (
    <div className="project-filter">
      <label htmlFor="category-select">Filter by category:</label>
      <select
        id="category-select"
        value={selectedCategory}
        onChange={(e) => setSelectedCategory(e.target.value)}
      >
        {allCategories.map(cat => (
          <option key={cat} value={cat}>
            {cat === "all" ? "All Categories" : cat.charAt(0).toUpperCase() + cat.slice(1)}
          </option>
        ))}
      </select>
    </div>
  );
};

export default ProjectFilter;
