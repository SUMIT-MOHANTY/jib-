import React from 'react';
import { motion } from 'framer-motion';
import { SkillsCategory } from '../../types/about';
import { staggerContainer, fadeInUp } from '../../utils/animationVariants';
import './SkillsDisplay.css';

interface Props {
 skillsData: SkillsCategory[];
}

const SkillsDisplay: React.FC<Props> = ({ skillsData }) => {
 return (
   <motion.div className="skills-display" variants={staggerContainer} initial="hidden" whileInView="visible" viewport={{ once: true }}>
     <h2 className="section-title">Skills & Expertise</h2>
     {skillsData.map((category, catIdx) => (
       <motion.div key={catIdx} className="skill-category" variants={fadeInUp}>
         <h3 className="category-name">{category.category}</h3>
         <div className="skills-grid">
           {category.skills.map((skill, idx) => (
             <div key={idx} className="skill-item">
               <div className="skill-header">
                 <span className="skill-name">{skill.name}</span>
                 <span className="skill-level">{skill.level}%</span>
               </div>
               <div className="skill-bar">
                 <motion.div className="skill-fill" initial={{ width: 0 }} whileInView={{ width: `${skill.level}%` }} transition={{ duration: 0.8, delay: idx * 0.1 }} />
               </div>
             </div>
           ))}
         </div>
       </motion.div>
     ))}
   </motion.div>
 );
};

export default SkillsDisplay;
