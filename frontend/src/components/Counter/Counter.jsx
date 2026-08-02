import React from "react";
import "./Counter.css";
import {
  FaProjectDiagram,
  FaUsers,
  FaAward,
  FaIndustry,
} from "react-icons/fa";

function Counter() {
  return (
    <section className="counter-section">
      
      {/* 🚀 FIXED LAYER: counter-overlay tag ko wapas jod diya taaki CSS background aur layout sahi se load ho sake */}
      <div className="counter-overlay">

        <div className="counter-heading">
          <span>OUR ACHIEVEMENTS</span>
          <h2>Numbers That Define Our Success</h2>
          <p>
            We are committed to delivering quality fabrication solutions with
            reliability, innovation and customer satisfaction.
          </p>
        </div>

        {/* 🚀 FIXED GRID MATRIX: Is wrapper div ke andar counter-grid class strictly 1 horizontal line layout force karegi */}
        <div className="counter-grid-wrapper-centered" style={{ width: "100%", display: "flex", justifyContent: "center" }}>
          <div className="counter-grid">

            <div className="counter-card">
              <FaAward className="counter-icon" />
              <h2>20+</h2>
              <p>Years Experience</p>
            </div>

            <div className="counter-card">
              <FaProjectDiagram className="counter-icon" />
              <h2>1000+</h2>
              <p>Projects Completed</p>
            </div>

            <div className="counter-card">
              <FaUsers className="counter-icon" />
              <h2>900+</h2>
              <p>Happy Clients</p>
            </div>

            <div className="counter-card">
              <FaIndustry className="counter-icon" />
              <h2>100+</h2>
              <p>Industrial Partners</p>
            </div>

          </div>
        </div>

      </div>

    </section>
  );
}

export default Counter;


