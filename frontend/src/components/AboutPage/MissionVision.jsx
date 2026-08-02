import "./MissionVision.css";
import { FaBullseye, FaEye, FaHandshake } from "react-icons/fa";

function MissionVision() {
  return (
    <section className="mission">

      <div className="mission-title">

        <span>OUR VALUES</span>

        <h2>Mission, Vision & Core Values</h2>

        <p>
          Our commitment is to deliver world-class fabrication solutions
          with quality, innovation and customer satisfaction.
        </p>

      </div>

      <div className="mission-grid">

        <div className="mission-card">

          <div className="mission-icon">
            <FaBullseye />
          </div>

          <h3>Our Mission</h3>

          <p>
            To provide high-quality fabrication services using modern
            technology, premium materials and skilled professionals.
          </p>

        </div>

        <div className="mission-card">

          <div className="mission-icon">
            <FaEye />
          </div>

          <h3>Our Vision</h3>

          <p>
            To become one of India's most trusted fabrication companies
            through innovation, quality and customer satisfaction.
          </p>

        </div>

        <div className="mission-card">

          <div className="mission-icon">
            <FaHandshake />
          </div>

          <h3>Core Values</h3>

          <p>
            Integrity, quality workmanship, timely delivery, safety and
            long-term customer relationships are the foundation of our business.
          </p>

        </div>

      </div>

    </section>
  );
}

export default MissionVision;

