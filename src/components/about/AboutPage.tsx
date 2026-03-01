import React from 'react';
import BiographyCard from './BiographyCard';
import SkillsDisplay from './SkillsDisplay';
import WorkExperienceTimeline from './WorkExperienceTimeline';
import EducationSection from './EducationSection';
import aboutData from '../../data/aboutData.json';
import skillsData from '../../data/skillsData.json';
import experienceData from '../../data/experienceData.json';
import educationData from '../../data/educationData.json';
import { BioData, SkillsCategory, WorkExperience, Education } from '../../types/about';
import './AboutPage.css';

const AboutPage: React.FC = () => {
 return (
   <div className="about-page">
     <div className="container">
       <BiographyCard bioData={aboutData as BioData} />
       <SkillsDisplay skillsData={skillsData as SkillsCategory[]} />
       <WorkExperienceTimeline experienceData={experienceData as WorkExperience[]} />
       <EducationSection educationData={educationData as Education[]} />
     </div>
   </div>
 );
};

export default AboutPage;
