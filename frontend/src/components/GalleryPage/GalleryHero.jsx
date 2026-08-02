import "./GalleryHero.css";
import { Link } from "react-router-dom";

function GalleryHero() {
  return (
    <section className="gallery-hero">

      <div className="gallery-overlay">

        <div className="gallery-content">

          <span>OUR PORTFOLIO</span>

          <h1>Our Completed Fabrication Projects</h1>

          <p>
            Explore our successfully completed fabrication projects including
            Steel Gates, Rolling Shutters, Industrial Sheds, Hydraulic Scissor
            Lifts, MS Railings and Custom Steel Structures.
          </p>

          <div className="gallery-buttons">

            <Link to="/contact" className="gallery-btn">
              Get Free Quote
            </Link>

            <Link to="/services" className="gallery-btn-outline">
              Our Services
            </Link>

          </div>

        </div>

      </div>

    </section>
  );
}

export default GalleryHero;

