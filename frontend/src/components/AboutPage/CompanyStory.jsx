import "./CompanyStory.css";
import { FaCheckCircle } from "react-icons/fa";

function CompanyStory() {
  return (
    <section className="company-story">

      <div className="company-container">

        <div className="company-image">
          <img
            src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=900&q=80"
            alt="Deepu Fabricator"
          />
        </div>

        <div className="company-content">

          <span>WHO WE ARE</span>

          <h2>
            Delivering Quality Fabrication Solutions Since 2005
          </h2>

          <p>
            Deepu Fabricator is a trusted fabrication company specializing
            in steel fabrication, industrial sheds, rolling shutters,
            hydraulic scissor lifts, staircases, railings and custom
            engineering solutions.
          </p>

          <p>
            Our experienced engineers and skilled workforce ensure every
            project is completed with precision, quality materials and
            on-time delivery.
          </p>

          <div className="company-list">

            <div>
              <FaCheckCircle />
              <span>Premium Quality Materials</span>
            </div>

            <div>
              <FaCheckCircle />
              <span>Experienced Fabrication Team</span>
            </div>

            <div>
              <FaCheckCircle />
              <span>Modern Machinery & Equipment</span>
            </div>

            <div>
              <FaCheckCircle />
              <span>On-Time Project Delivery</span>
            </div>

          </div>

          <button className="story-btn">
            Learn More
          </button>

        </div>

      </div>

    </section>
  );
}

export default CompanyStory;

