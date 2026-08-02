import React, { useState, useEffect } from "react";
import API from "../../api/axios";
import "./Projects.css";

// 🚀 EXACT MATCH: Aapke folders ke real image path tokens setup
import gate1Img from "../../assets/gallery/gate1.jpg";
import gate2Img from "../../assets/gallery/gate2.jpg";
import lift1Img from "../../assets/gallery/lift1.jpg";
import railing1Img from "../../assets/gallery/railing1.jpg";
import shed1Img from "../../assets/gallery/shed1.jpg";
import shed2Img from "../../assets/gallery/shed2.jpg";
import shutter1Img from "../../assets/gallery/shutter1.jpg";
import staircase1Img from "../../assets/gallery/staircase1.jpg";

function Projects() {
  const [dbProjects, setDbProjects] = useState([]);
  const [loading, setLoading] = useState(true);

  // 🌟 8 Beautiful Industrial Standard Showcase Fallback Items Grid Cache
  const localFallbackProjects = [
    { id: "fb_1", title: "Modern Safety Boundary Gate", category: "Steel Gate / Grill Work", image_url: gate1Img, isLocal: true },
    { id: "fb_2", title: "Premium Designer Entrance Gate", category: "Steel Gate / Grill Work", image_url: gate2Img, isLocal: true },
    { id: "fb_3", title: "Hydraulic Scissor Lift Platform", category: "Hydraulic Scissor Lift", image_url: lift1Img, isLocal: true },
    { id: "fb_4", title: "Architectural Staircase Railing", category: "Steel Gate / Grill Work", image_url: railing1Img, isLocal: true },
    { id: "fb_5", title: "Heavy Structural Industrial Shed", category: "Industrial Shed Construction", image_url: shed1Img, isLocal: true },
    { id: "fb_6", title: "Commercial Warehouse Extension Shed", category: "Industrial Shed Construction", image_url: shed2Img, isLocal: true },
    { id: "fb_7", title: "Automatic Rolling Shutter Door", category: "Rolling Shutter Installation", image_url: shutter1Img, isLocal: true },
    { id: "fb_8", title: "Modern Metal Floating Staircase", category: "Other Fabrication Work", image_url: staircase1Img, isLocal: true }
  ];

  const fetchLivePortfolio = async () => {
    try {
      const response = await API.get("/gallery/");
      const result = response.data;
      if (result.status === "success" && result.data.length > 0) {
        setDbProjects(result.data);
      } else {
        setDbProjects([]);
      }
    } catch (error) {
      console.error("Database khali hai, using static cards grid framework data vectors.");
      setDbProjects([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLivePortfolio();
  }, []);

  if (loading) {
    return (
      <section className="projects" style={{ textAlign: "center", padding: "100px 20px" }}>
        <p style={{ color: "#111827", fontSize: "1.2rem", fontWeight: "bold" }}>Syncing Portfolio Images from Warehouse DB Grid...</p>
      </section>
    );
  }

  const finalDisplayData = dbProjects.length > 0 ? dbProjects : localFallbackProjects;

  return (
    <section className="projects">
      <div className="container">
        <div className="section-header">
          <span className="section-subtitle">OUR PROJECTS</span>
          <h2 className="section-title">Recent Fabrication Work</h2>
          <p className="section-desc">
            Explore some of our completed fabrication projects delivered
            with precision, quality and modern engineering.
          </p>
        </div>

        <div className="projects-grid">
          {finalDisplayData.map((project) => {
            const finalImageSrc = project.isLocal
              ? project.image_url
              : `${project.image_url}`;

            return (
              <div className="project-card" key={project.id || project.title}>
                <div className="project-img-wrapper">
                  <img
                    src={finalImageSrc}
                    alt={project.title}
                    loading="lazy"
                  />
                  <div className="project-overlay">
                    <span className="project-category">{project.category}</span>
                    <h3>{project.title}</h3>
                    <button className="project-view-btn">View Project</button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default Projects;






