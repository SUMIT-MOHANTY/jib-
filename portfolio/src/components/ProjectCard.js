import React from "react";
import "./ProjectCard.css";

const ProjectCard = ({ project }) => {
  const { title, description, image, technologies, liveUrl, sourceUrl, category } = project;

  const handleLinkClick = (url, linkType) => {
    if (!url) {
      alert(`${linkType} link not available`);
      return;
    }
    window.open(url, "_blank", "noopener,noreferrer");
  };

  return (
    <article className="project-card">
      <div className="project-image">
        {image ? <img src={image} alt={title} /> : <div className="placeholder-image">No Image</div>}
      </div>
      <div className="project-content">
        <span className="project-category">{category}</span>
        <h3 className="project-title">{title}</h3>
        <p className="project-description">{description}</p>
        <div className="project-technologies">
          {technologies?.map((tech, index) => (
            <span key={index} className="tech-tag">{tech}</span>
          ))}
        </div>
        <div className="project-links">
          <button onClick={() => handleLinkClick(liveUrl, "Live")} className="btn-live">Live Demo</button>
          <button onClick={() => handleLinkClick(sourceUrl, "Source")} className="btn-source">Source Code</button>
        </div>
      </div>
    </article>
  );
};

export default ProjectCard;
