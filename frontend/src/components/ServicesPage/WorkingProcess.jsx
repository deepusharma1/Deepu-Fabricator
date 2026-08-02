import "./WorkingProcess.css";
import {
  FaClipboardCheck,
  FaDraftingCompass,
  FaTools,
  FaHardHat,
  FaTruck,
} from "react-icons/fa";

const process = [
  {
    icon: <FaClipboardCheck />,
    title: "Consultation",
    desc: "Understand client requirements and site inspection."
  },
  {
    icon: <FaDraftingCompass />,
    title: "Design",
    desc: "Prepare detailed drawings and fabrication plan."
  },
  {
    icon: <FaTools />,
    title: "Fabrication",
    desc: "Manufacture products using advanced machinery."
  },
  {
    icon: <FaHardHat />,
    title: "Installation",
    desc: "Professional on-site installation by our experts."
  },
  {
    icon: <FaTruck />,
    title: "Delivery",
    desc: "Timely delivery with quality assurance."
  }
];

function WorkingProcess() {
  return (
    <section className="process">

      <div className="process-title">
        <span>HOW WE WORK</span>
        <h2>Our Working Process</h2>
        <p>
          We follow a systematic process to ensure every fabrication project
          is completed with precision, safety, and customer satisfaction.
        </p>
      </div>

      <div className="process-grid">

        {process.map((step, index) => (

          <div className="process-card" key={index}>

            <div className="process-number">
              {index + 1}
            </div>

            <div className="process-icon">
              {step.icon}
            </div>

            <h3>{step.title}</h3>

            <p>{step.desc}</p>

          </div>

        ))}

      </div>

    </section>
  );
}

export default WorkingProcess;

