import "./Team.css";
import {
  FaFacebookF,
  FaLinkedinIn,
  FaInstagram,
  FaUserTie,
} from "react-icons/fa";

const team = [
  {
    name: "Mr. Suryabhan Sharma",
    role: "Founder & Director",
  },
  {
    name: "Mr. Deepu Sharma",
    role: "Project Manager",
  },
  {
    name: "Amit Verma",
    role: "Site Engineer",
  },
  {
    name: "Vikas Singh",
    role: "Production Supervisor",
  },
];

function Team() {
  return (
    <section className="team">

      <div className="team-title">
        <span>OUR TEAM</span>

        <h2>Meet Our Experts</h2>

        <p>
          Our experienced professionals are committed to delivering
          high-quality fabrication solutions with precision and safety.
        </p>
      </div>

      <div className="team-grid">

        {team.map((member, index) => (

          <div className="team-card" key={index}>

            <div className="team-avatar">
              <FaUserTie />
            </div>

            <h3>{member.name}</h3>

            <span>{member.role}</span>

            <div className="team-social">

              <a href="#">
                <FaFacebookF />
              </a>

              <a href="#">
                <FaLinkedinIn />
              </a>

              <a href="#">
                <FaInstagram />
              </a>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}

export default Team;

