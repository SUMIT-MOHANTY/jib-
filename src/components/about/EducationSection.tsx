import React from 'react';
import { motion } from 'framer-motion';
import { Education } from '../../types/about';
import { staggerContainer, scaleIn } from '../../utils/animationVariants';
import './EducationSection.css';

interface Props {
 educationData: Education[];
}

const EducationSection: React.FC<Props> = ({ educationData }) => {
 return (
   <motion.div className="education-section" variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
     <h2 className="section-title">Education</h2>
     <div className="education-grid">
       {educationData.map((edu, idx) => (
         <motion.div key={edu.id} className="education-card" variants={scaleIn}>
           <div className="edu-header">
             <h3 className="institution">{edu.institution}</h3>
             <span className="dates">{edu.startDate} -- {edu.endDate}</span>
           </div>
           <p className="degree">{edu.degree}</p>
           <p className="field">{edu.field}</p>
           {edu.gpa && <p className="gpa">GPA: {edu.gpa}</p>}
           {edu.achievements && edu.achievements.length > 0 && (
             <ul className="achievements">
               {edu.achievements.map((a, i) => <li key={i}>{a}</li>)}
             </ul>
           )}
         </motion.div>
       ))}
     </div>
   </motion.div>
 );
};

export default EducationSection;
