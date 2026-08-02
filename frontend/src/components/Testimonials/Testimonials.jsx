import "./Testimonials.css";
import { FaStar } from "react-icons/fa";

const testimonials = [
  {
    name: "Rajesh Kumar",
    company: "Industrial Client",
    review:
      "Deepu Fabricator delivered our steel structure project on time with excellent workmanship. Highly recommended!",
  },
  {
    name: "Amit Sharma",
    company: "Construction Company",
    review:
      "Professional team, quality fabrication, and excellent customer support throughout the project.",
  },
  {
    name: "Sunil Verma",
    company: "Factory Owner",
    review:
      "We purchased a hydraulic scissor lift and are extremely satisfied with its quality and performance.",
  },
];

function Testimonials() {
  return (
    <section className="testimonials">

      <div className="testimonial-title">
        <span>TESTIMONIALS</span>
        <h2>What Our Clients Say</h2>
        <p>
          Customer satisfaction is our biggest achievement. Here are some
          reviews from our valuable clients.
        </p>
      </div>

      <div className="testimonial-grid">

        {testimonials.map((item, index) => (
          <div className="testimonial-card" key={index}>

            <div className="stars">
              <FaStar />
              <FaStar />
              <FaStar />
              <FaStar />
              <FaStar />
            </div>

            <p className="review">
              "{item.review}"
            </p>

            <div className="client">
              <div className="avatar">
                {item.name.charAt(0)}
              </div>

              <div>
                <h4>{item.name}</h4>
                <span>{item.company}</span>
              </div>
            </div>

          </div>
        ))}

      </div>

    </section>
  );
}

export default Testimonials;

