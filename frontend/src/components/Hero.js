import React from 'react';
import { motion } from 'framer-motion';
import './Hero.css';

const Hero = () => {
  const scrollToContact = () => {
    document.getElementById('contact').scrollIntoView({ behavior: 'smooth' });
  };

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.2, delayChildren: 0.3 }
    }
  };

  const itemVariants = {
    hidden: { y: 30, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: { type: 'spring', stiffness: 100, damping: 12 }
    }
  };

  const buttonVariants = {
    hidden: { scale: 0, opacity: 0 },
    visible: {
      scale: 1,
      opacity: 1,
      transition: { delay: 1, type: 'spring', stiffness: 200 }
    },
    hover: { scale: 1.05, transition: { duration: 0.2 } },
    tap: { scale: 0.95 }
  };

  const floatingVariants = {
    animate: {
      y: [0, -20, 0],
      transition: { repeat: Infinity, duration: 3, ease: 'easeInOut' }
    }
  };

  return (
    <section className="hero">
      <div className="hero-bg">
        <motion.div 
          className="floating-shape shape-1"
          variants={floatingVariants}
          animate="animate"
        />
        <motion.div 
          className="floating-shape shape-2"
          variants={floatingVariants}
          animate="animate"
          style={{ animationDelay: '1s' }}
        />
        <motion.div 
          className="floating-shape shape-3"
          variants={floatingVariants}
          animate="animate"
          style={{ animationDelay: '2s' }}
        />
      </div>

      <motion.div 
        className="hero-content"
        variants={containerVariants}
        initial="hidden"
        animate="visible"
      >
        <motion.span className="hero-badge" variants={itemVariants}>
          ✨ Welcome to Our Platform
        </motion.span>

        <motion.h1 className="hero-title" variants={itemVariants}>
          Build Something
          <span className="gradient-text"> Amazing </span>
          Today
        </motion.h1>

        <motion.p className="hero-subtitle" variants={itemVariants}>
          Transform your ideas into reality with our cutting-edge solutions. 
          We help businesses innovate, grow, and succeed in the digital age.
        </motion.p>

        <motion.div className="hero-buttons" variants={itemVariants}>
          <motion.button
            className="btn btn-primary"
            variants={buttonVariants}
            whileHover="hover"
            whileTap="tap"
            onClick={scrollToContact}
          >
            Get Started
          </motion.button>
          <motion.button
            className="btn btn-secondary"
            variants={buttonVariants}
            whileHover="hover"
            whileTap="tap"
          >
            Learn More
          </motion.button>
        </motion.div>

        <motion.div className="hero-stats" variants={itemVariants}>
          <div className="stat">
            <span className="stat-number">10K+</span>
            <span className="stat-label">Clients</span>
          </div>
          <div className="stat-divider" />
          <div className="stat">
            <span className="stat-number">99%</span>
            <span className="stat-label">Satisfaction</span>
          </div>
          <div className="stat-divider" />
          <div className="stat">
            <span className="stat-number">24/7</span>
            <span className="stat-label">Support</span>
          </div>
        </motion.div>
      </motion.div>

      <motion.div 
        className="scroll-indicator"
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 2, duration: 0.5 }}
      >
        <motion.div
          animate={{ y: [0, 8, 0] }}
          transition={{ repeat: Infinity, duration: 1.5 }}
        >
          <span>↓</span>
        </motion.div>
      </motion.div>
    </section>
  );
};

export default Hero;
