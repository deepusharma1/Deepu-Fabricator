import "./ServiceHero.css";

function ServiceHero() {
  return (
    <section className="service-hero">
      <div className="service-overlay">

        <div className="service-content">

          <span>OUR SERVICES</span>

          <h1>Professional Steel Fabrication Services</h1>

          <p>
            Deepu Fabricator provides complete steel fabrication solutions
            including Gates, Rolling Shutters, Industrial Sheds,
            Hydraulic Scissor Lifts, Railings, Staircases,
            Structural Fabrication and Custom Engineering Works.
          </p>

          <div className="service-buttons">

            <a href="/contact" className="primary-btn">
              Get Free Quote
            </a>

            <a href="/gallery" className="secondary-btn">
              View Projects
            </a>

          </div>

        </div>

      </div>
    </section>
  );
}

export default ServiceHero; 

