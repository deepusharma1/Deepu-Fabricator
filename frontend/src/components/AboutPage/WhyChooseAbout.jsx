import "./WhyChooseAbout.css";
import {
  FaCheckCircle,
  FaHardHat,
  FaTruck,
  FaShieldAlt,
  FaUsers,
  FaTools,
} from "react-icons/fa";

const features = [
  {
    icon: <FaHardHat />,
    title: "Experienced Engineers",
    desc: "Our skilled engineers ensure every project meets high industry standards.",
  },
  {
    icon: <FaTools />,
    title: "Advanced Machinery",
    desc: "We use modern fabrication equipment for precise and efficient work.",
  },
  {
    icon: <FaShieldAlt />,
    title: "Quality Assurance",
    desc: "Every product undergoes strict quality checks before delivery.",
  },
  {
    icon: <FaTruck />,
    title: "On-Time Delivery",
    desc: "We are committed to completing and delivering projects on schedule.",
  },
  {
    icon: <FaUsers />,
    title: "Customer Satisfaction",
    desc: "We build long-term relationships through reliable service and support.",
  },
  {
    icon: <FaCheckCircle />,
    title: "Affordable Pricing",
    desc: "Competitive pricing without compromising on quality.",
  },
];

function WhyChooseAbout() {
  return (
    <section className="why-about">

      <div className="why-title">
        <span>WHY CHOOSE US</span>
        <h2>Why Choose Deepu Fabricator?</h2>
        <p>
          We combine expertise, innovation, quality materials, and dedicated
          customer support to deliver reliable fabrication solutions.
        </p>
      </div>

      <div className="why-grid">
        {features.map((item, index) => (
          <div className="why-card" key={index}>
            <div className="why-icon">{item.icon}</div>
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
          </div>
        ))}
      </div>

    </section>
  );
}

export default WhyChooseAbout;

