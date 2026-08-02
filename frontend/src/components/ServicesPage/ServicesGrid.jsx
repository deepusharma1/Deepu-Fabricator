import "./ServicesGrid.css";
import {
  FaDoorOpen,
  FaWarehouse,
  FaIndustry,
  FaBuilding,
  FaTools,
  FaHardHat,
  FaCogs,
  FaWrench,
  FaArrowRight,
} from "react-icons/fa";

const services = [
  {
    icon: <FaDoorOpen />,
    title: "Steel Gates",
    desc: "Custom designed residential and industrial steel gates."
  },
  {
    icon: <FaWarehouse />,
    title: "Rolling Shutters",
    desc: "Heavy-duty rolling shutters for shops and warehouses."
  },
  {
    icon: <FaIndustry />,
    title: "Hydraulic Scissor Lifts",
    desc: "Industrial hydraulic lifting platforms."
  },
  {
    icon: <FaBuilding />,
    title: "Industrial Sheds",
    desc: "PEB and industrial shed fabrication services."
  },
  {
    icon: <FaTools />,
    title: "MS Railings",
    desc: "Modern mild steel railings for homes and offices."
  },
  {
    icon: <FaHardHat />,
    title: "Steel Staircases",
    desc: "Strong and elegant staircase fabrication."
  },
  {
    icon: <FaCogs />,
    title: "Structural Fabrication",
    desc: "Industrial steel structures and fabrication."
  },
  {
    icon: <FaWrench />,
    title: "Maintenance Services",
    desc: "Repair and maintenance of fabricated structures."
  }
];

function ServicesGrid() {
  return (
    <section className="services-grid-section">

      <div className="section-title">
        <span>WHAT WE DO</span>
        <h2>Our Professional Services</h2>
        <p>
          We provide complete steel fabrication solutions with premium
          quality, modern machinery and experienced engineers.
        </p>
      </div>

      <div className="services-grid">

        {services.map((item, index) => (

          <div className="service-card" key={index}>

            <div className="service-icon">
              {item.icon}
            </div>

            <h3>{item.title}</h3>

            <p>{item.desc}</p>

            <button>
              Learn More <FaArrowRight />
            </button>

          </div>

        ))}

      </div>

    </section>
  );
}

export default ServicesGrid;

