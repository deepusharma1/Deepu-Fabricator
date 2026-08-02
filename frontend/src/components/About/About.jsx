import "./About.css";
import { FaCheckCircle } from "react-icons/fa";

function About() {
  return (
    <section className="about-section">
      <div className="container about-container">

        <div className="about-image">
          <img
            src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1200&q=80"
            alt="Deepu Fabricator"
          />
        </div>

        <div className="about-content">

          <span className="about-subtitle">
            ABOUT OUR COMPANY
          </span>

          <h2>
            We Build Strong, Reliable & Modern Fabrication Solutions
          </h2>

          <p>
            Deepu Fabricator is a trusted name in steel fabrication,
            rolling shutters, hydraulic cranes, scissor lifts,
            aluminium works, industrial sheds, gates and custom
            fabrication projects.
          </p>

          <p>
            With years of experience and skilled professionals,
            we deliver high-quality fabrication work using
            premium materials and modern equipment.
          </p>

          <div className="about-list">

            <div>
              <FaCheckCircle />
              Premium Quality Materials
            </div>

            <div>
              <FaCheckCircle />
              Skilled Engineers
            </div>

            <div>
              <FaCheckCircle />
              Timely Delivery
            </div>

            <div>
              <FaCheckCircle />
              Affordable Pricing
            </div>

          </div>

          <div className="about-counter">

            <div>
              <h3>20+</h3>
              <p>Years Experience</p>
            </div>

            <div>
              <h3>1000+</h3>
              <p>Projects Completed</p>
            </div>

            <div>
              <h3>900+</h3>
              <p>Happy Clients</p>
            </div>

          </div>

          <button className="about-btn">
            Learn More
          </button>

        </div>

      </div>
    </section>
  );
}

export default About;


