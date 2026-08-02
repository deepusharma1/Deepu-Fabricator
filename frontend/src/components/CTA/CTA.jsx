import "./CTA.css";
import { FaPhoneAlt, FaWhatsapp, FaEnvelope } from "react-icons/fa";

function CTA() {
  return (
    <section className="cta">

      <div className="cta-overlay">

        <div className="cta-content">

          <span>GET STARTED TODAY</span>

          <h2>
            Looking for Reliable Fabrication Services?
          </h2>

          <p>
            Deepu Fabricator specializes in Steel Gates, Rolling Shutters,
            Industrial Sheds, Hydraulic Scissor Lifts, Railings,
            Staircases and Custom Fabrication.
          </p>

          <div className="cta-buttons">

            <a href="tel:+919958431462" className="btn phone">
              <FaPhoneAlt />
              Call Now
            </a>

            <a
              href="https://wa.me/919958431462"
              target="_blank"
              rel="noreferrer"
              className="btn whatsapp"
            >
              <FaWhatsapp />
              WhatsApp
            </a>

            <a
              href="mailto:info@deepufabricator.com"
              className="btn email"
            >
              <FaEnvelope />
              Email Us
            </a>

          </div>

        </div>

      </div>

    </section>
  );
}

export default CTA;

