import "./Certificates.css";
import {
  FaCertificate,
  FaShieldAlt,
  FaAward,
  FaCheckCircle,
} from "react-icons/fa";

function Certificates() {
  return (
    <section className="certificates">

      <div className="certificate-title">

        <span>QUALITY & TRUST</span>

        <h2>Certificates & Trusted Clients</h2>

        <p>
          We are committed to delivering high-quality fabrication work
          while maintaining industry standards and customer satisfaction.
        </p>

      </div>

      <div className="certificate-grid">

        <div className="certificate-card">
          <div className="certificate-icon">
            <FaCertificate />
          </div>

          <h3>ISO Standards</h3>

          <p>
            Our work follows recognized quality management practices to
            ensure reliable fabrication solutions.
          </p>
        </div>

        <div className="certificate-card">
          <div className="certificate-icon">
            <FaShieldAlt />
          </div>

          <h3>Safety First</h3>

          <p>
            Every project is completed by following strict workplace
            safety guidelines.
          </p>
        </div>

        <div className="certificate-card">
          <div className="certificate-icon">
            <FaAward />
          </div>

          <h3>Quality Assurance</h3>

          <p>
            Every product is inspected before delivery to maintain
            superior quality.
          </p>
        </div>

        <div className="certificate-card">
          <div className="certificate-icon">
            <FaCheckCircle />
          </div>

          <h3>Trusted by Clients</h3>

          <p>
            Hundreds of customers trust Deepu Fabricator for industrial
            and residential fabrication work.
          </p>
        </div>

      </div>

      <div className="client-section">

        <h3>Our Valued Clients</h3>

        <div className="client-logos">

          <div className="client-logo">ABC Industries</div>

          <div className="client-logo">XYZ Builders</div>

          <div className="client-logo">Steel Tech</div>

          <div className="client-logo">Metro Infra</div>

          <div className="client-logo">Prime Engineering</div>

        </div>

      </div>

    </section>
  );
}

export default Certificates;

