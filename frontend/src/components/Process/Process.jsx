import React from "react";
import "./Process.css";
import {
  FaPhoneAlt,
  FaDraftingCompass,
  FaTools,
  FaTruck,
} from "react-icons/fa";

const steps = [
  {
    icon: <FaPhoneAlt />,
    title: "Consultation",
    description: "Discuss your project requirements."
  },
  {
    icon: <FaDraftingCompass />,
    title: "Design",
    description: "Prepare drawings and planning."
  },
  {
    icon: <FaTools />,
    title: "Fabrication",
    description: "Manufacturing with premium materials."
  },
  {
    icon: <FaTruck />,
    title: "Installation",
    description: "Delivery and installation at site."
  }
];

function Process() {
  return (
    <section className="process">

      <div className="process-title">
        <h2>Our Working Process</h2>
        <p>Simple four step fabrication process.</p>
      </div>

      {/* 🎯 FIXED WRAPPER CONTEXT: Pure tags distribution structure ko page center alignment par lock kiya */}
      <div className="process-grid-wrapper-centered" style={{ width: "100%", display: "flex", justifyContent: "center" }}>
        <div className="process-grid">

          {steps.map((step, index) => (
            <div className="process-card" key={index}>
              <div className="process-icon">
                {step.icon}
              </div>

              <h3>{step.title}</h3>
              <p>{step.description}</p>
            </div>
          ))}

        </div>
      </div>

    </section>
  );
}

export default Process;


