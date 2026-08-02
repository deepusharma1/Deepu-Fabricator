import "./Industries.css";
import {
  FaIndustry,
  FaBuilding,
  FaWarehouse,
  FaTruckMoving,
  FaHome,
  FaTools,
} from "react-icons/fa";

const industries = [
  {
    icon: <FaIndustry />,
    title: "Manufacturing",
    description: "Custom fabrication solutions for manufacturing industries.",
  },
  {
    icon: <FaBuilding />,
    title: "Construction",
    description: "Steel structures, railings, sheds and fabrication work.",
  },
  {
    icon: <FaWarehouse />,
    title: "Warehousing",
    description: "Warehouse sheds, storage platforms and heavy structures.",
  },
  {
    icon: <FaTruckMoving />,
    title: "Logistics",
    description: "Loading platforms, scissor lifts and handling equipment.",
  },
  {
    icon: <FaHome />,
    title: "Residential",
    description: "Modern gates, staircases, railings and balconies.",
  },
  {
    icon: <FaTools />,
    title: "Custom Projects",
    description: "Tailor-made fabrication according to customer needs.",
  },
];

function Industries() {
  return (
    <section className="industries">

      <div className="industries-title">
        <span>INDUSTRIES WE SERVE</span>

        <h2>Serving Every Industry with Quality Fabrication</h2>

        <p>
          We provide fabrication services for residential, commercial and industrial sectors with high-quality workmanship.
        </p>
      </div>

      <div className="industries-grid">
        {industries.map((item, index) => (
          <div className="industry-card" key={index}>

            <div className="industry-icon">
              {item.icon}
            </div>

            <h3>{item.title}</h3>

            <p>{item.description}</p>

          </div>
        ))}
      </div>

    </section>
  );
}

export default Industries;

