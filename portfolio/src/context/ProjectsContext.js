import React, { createContext, useState, useEffect, useContext } from "react";
import { fetchProjects, fetchCategories } from "../services/api";

const ProjectsContext = createContext();

export const useProjects = () => useContext(ProjectsContext);

export const ProjectsProvider = ({ children }) => {
  const [projects, setProjects] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const [projectsData, categoriesData] = await Promise.all([
          fetchProjects(),
          fetchCategories()
        ]);
        setProjects(projectsData);
        setCategories(categoriesData);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  const filteredProjects = selectedCategory === "all"
    ? projects
    : projects.filter(p => p.category === selectedCategory);

  return (
    <ProjectsContext.Provider value={{
      projects: filteredProjects,
      categories,
      selectedCategory,
      setSelectedCategory,
      loading,
      error
    }}>
      {children}
    </ProjectsContext.Provider>
  );
};
