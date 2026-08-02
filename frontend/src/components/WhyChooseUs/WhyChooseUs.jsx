import "./WhyChooseUs.css";
import {
  FaAward,
  FaUsers,
  FaClock,
  FaShieldAlt,
} from "react-icons/fa";

function WhyChooseUs() {
  return (
    <section className="why">

      <div className="why-heading">

        <span>WHY CHOOSE US</span>

        <h2>Trusted Fabrication Partner</h2>

        <p>
          We provide reliable fabrication solutions using advanced technology,
          experienced professionals and premium quality materials.
        </p>

      </div>

      <div className="why-container">

        <div className="why-card">
          <FaAward className="icon" />
          <h3>Premium Quality</h3>
          <p>
            We use only high-quality steel, aluminium and industrial materials.
          </p>
        </div>

        <div className="why-card">
          <FaUsers className="icon" />
          <h3>Expert Team</h3>
          <p>
            Experienced engineers and skilled fabricators deliver every project
            with precision.
          </p>
        </div>

        <div className="why-card">
          <FaClock className="icon" />
          <h3>On-Time Delivery</h3>
          <p>
            Every project is completed within the committed timeline without
            compromising quality.
          </p>
        </div>

        <div className="why-card">
          <FaShieldAlt className="icon" />
          <h3>Trusted Service</h3>
          <p>
            Hundreds of satisfied customers trust us for industrial and
            commercial fabrication work.
          </p>
        </div>

      </div>

    </section>
  );
}

export default WhyChooseUs;

