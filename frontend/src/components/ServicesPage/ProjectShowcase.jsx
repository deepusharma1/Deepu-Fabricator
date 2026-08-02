import "./ProjectShowcase.css";

const projects = [
  {
    title: "Steel Gates",
    image:
      "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=900&q=80",
    description: "Custom fabricated residential and industrial steel gates.",
  },
  {
    title: "Rolling Shutters",
    image:
      "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=900&q=80",
    description: "Heavy-duty rolling shutters for commercial buildings.",
  },
  {
    title: "Industrial Shed",
    image:
      "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=900&q=80",
    description: "PEB and industrial shed fabrication solutions.",
  },
  {
    title: "Hydraulic Scissor Lift",
    image:
      "https://images.unsplash.com/photo-1513828583688-c52646db42da?auto=format&fit=crop&w=900&q=80",
    description: "Hydraulic lifting platforms for industrial applications.",
  },
  {
    title: "MS Railings",
    image:
      "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6?auto=format&fit=crop&w=900&q=80",
    description: "Modern mild steel railings for residential and commercial projects.",
  },
  {
    title: "Steel Staircase",
    image:
      "https://images.unsplash.com/photo-1511818966892-d7d671e672a2?auto=format&fit=crop&w=900&q=80",
    description: "Strong and elegant custom steel staircase fabrication.",
  },
];

function ProjectShowcase() {
  return (
    <section className="project-showcase">

      <div className="project-title">
        <span>OUR PROJECTS</span>

        <h2>Featured Fabrication Projects</h2>

        <p>
          We deliver high-quality fabrication projects with precision,
          durability and customer satisfaction.
        </p>
      </div>

      <div className="project-grid">

        {projects.map((project, index) => (
          <div className="project-card" key={index}>

            <img
              src={project.image}
              alt={project.title}
            />

            <div className="project-overlay">

              <h3>{project.title}</h3>

              <p>{project.description}</p>

              <button>View Project</button>

            </div>

          </div>
        ))}

      </div>

    </section>
  );
}

export default ProjectShowcase;

