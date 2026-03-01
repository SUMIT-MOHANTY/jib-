import React from 'react';
import { motion } from 'framer-motion';
import { BioData } from '../../types/about';
import { fadeIn } from '../../utils/animationVariants';
import './BiographyCard.css';

interface Props {
 bioData: BioData;
}

const BiographyCard: React.FC<Props> = ({ bioData }) => {
 return (
   <motion.div className="biography-card" variants={fadeIn} initial="hidden" animate="visible">
     <div className="profile-section">
       <img src={bioData.profileImage} alt={bioData.name} className="profile-image" />
       <div className="profile-info">
         <h1 className="name">{bioData.name}</h1>
         <h2 className="title">{bioData.title}</h2>
         <p className="location">{bioData.location}</p>
         <a href={`mailto:${bioData.email}`} className="email">{bioData.email}</a>
         <div className="social-links">
           {bioData.socialLinks.linkedin && <a href={bioData.socialLinks.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn</a>}
           {bioData.socialLinks.github && <a href={bioData.socialLinks.github} target="_blank" rel="noopener noreferrer">GitHub</a>}
           {bioData.socialLinks.twitter && <a href={bioData.socialLinks.twitter} target="_blank" rel="noopener noreferrer">Twitter</a>}
         </div>
       </div>
     </div>
     <p className="biography">{bioData.biography}</p>
   </motion.div>
 );
};

export default BiographyCard;
