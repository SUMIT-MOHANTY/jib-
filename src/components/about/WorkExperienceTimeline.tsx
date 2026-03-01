import React from 'react';
import { motion } from 'framer-motion';
import { WorkExperience } from '../../types/about';
import { staggerContainer, slideInLeft } from '../../utils/animationVariants';
import './WorkExperienceTimeline.css';

interface Props {
 experienceData: WorkExperience[];
}

const WorkExperienceTimeline: React.FC<Props> = ({ experienceData }) => {
 return (
   <motion.div className="experience-timeline" variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
     <h2 className="section-title">Work Experience</h2>
     <div className="timeline">
       {experienceData.map((exp, idx) => (
         <motion.div key={exp.id} className="timeline-item" variants={slideInLeft}>
           <div className="timeline-dot"></div>
           <div className="timeline-content">
             <div className="timeline-header">
               <h3 className="company">{exp.company}</h3>
               <span className="dates">{exp.startDate} -- {exp.endDate || 'Present'}</span>
             </div>
             <h4 className="role">{exp.role}</h4>
             <p className="location">{exp.location}</p>
             <p className="description">{exp.description}</p>
             <ul className="highlights">
               {exp.highlights.map((h, i) => <li key={i}>{h}</li>)}
             </ul>
           </div>
         </motion.div>
       ))}
     </div>
   </motion.div>
 );
};

export default WorkExperienceTimeline;
