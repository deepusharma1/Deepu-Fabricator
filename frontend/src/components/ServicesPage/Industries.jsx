import "./Industries.css";
import {
  FaHome,
  FaBuilding,
  FaIndustry,
  FaWarehouse,
  FaHospital,
  FaSchool,
} from "react-icons/fa";

const industries = [
  {
    icon: <FaHome />,
    title: "Residential",
    desc: "Steel Gates, Railings, Staircases, Balconies and Home Fabrication.",
  },
  {
    icon: <FaBuilding />,
    title: "Commercial",
    desc: "Office Buildings, Showrooms, Shopping Complexes and Malls.",
  },
  {
    icon: <FaIndustry />,
    title: "Industrial",
    desc: "Factory Structures, Heavy Fabrication and Industrial Projects.",
  },
  {
    icon: <FaWarehouse />,
    title: "Warehouses",
    desc: "Warehouse Structures, Rolling Shutters and Steel Platforms.",
  },
  {
    icon: <FaHospital />,
    title: "Hospitals",
    desc: "Medical Equipment Supports, Railings and Safety Structures.",
  },
  {
    icon: <FaSchool />,
    title: "Educational Institutes",
    desc: "School & College Gates, Railings, Staircases and Shade Structures.",
  },
];

function Industries() {
  return (
    <section className="industries">

      <div className="industries-title">

        <span>OUR EXPERTISE</span>

        <h2>Industries We Serve</h2>

        <p>
          Deepu Fabricator proudly provides fabrication services for
          residential, commercial and industrial sectors with high-quality
          workmanship and timely delivery.
        </p>

      </div>

      <div className="industries-grid">

        {industries.map((item, index) => (

          <div className="industry-card" key={index}>

            <div className="industry-icon">

              {item.icon}

            </div>

            <h3>{item.title}</h3>

            <p>{item.desc}</p>

          </div>

        ))}

      </div>

    </section>
  );
}

export default Industries;

