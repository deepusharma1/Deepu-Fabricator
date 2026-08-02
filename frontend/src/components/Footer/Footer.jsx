import { Link } from "react-router-dom";
import "./Footer.css";

import {
  FaFacebookF,
  FaInstagram,
  FaLinkedinIn,
  FaYoutube,
  FaPhoneAlt,
  FaEnvelope,
  FaMapMarkerAlt,
} from "react-icons/fa";


function Footer() {

  return (

    <footer className="footer">

      <div className="container footer-container">


        {/* Company */}
        <div className="footer-box">

          <h2>
            Deepu Fabricator
          </h2>

          <p>
            We provide premium fabrication solutions including Steel Gates,
            Rolling Shutters, Industrial Sheds, Hydraulic Scissor Lifts,
            Railings and Custom Fabrication.
          </p>


          <div className="social-icons">

            <a href="#" aria-label="Facebook">
              <FaFacebookF />
            </a>

            <a href="#" aria-label="Instagram">
              <FaInstagram />
            </a>

            <a href="#" aria-label="LinkedIn">
              <FaLinkedinIn />
            </a>

            <a href="#" aria-label="Youtube">
              <FaYoutube />
            </a>

          </div>

        </div>



        {/* Quick Links */}
        <div className="footer-box">

          <h3>
            Quick Links
          </h3>

          <ul>

            <li><Link to="/">Home</Link></li>

            <li><Link to="/about">About</Link></li>

            <li><Link to="/services">Services</Link></li>

            <li><Link to="/gallery">Gallery</Link></li>

            <li><Link to="/contact">Contact</Link></li>

          </ul>

        </div>




        {/* Services */}
        <div className="footer-box">

          <h3>
            Our Services
          </h3>

          <ul>

            <li>Steel Gates</li>
            <li>Rolling Shutters</li>
            <li>Industrial Shed</li>
            <li>Hydraulic Scissor Lift</li>
            <li>MS Railing</li>
            <li>Custom Fabrication</li>

          </ul>

        </div>




        {/* Contact */}
        <div className="footer-box">

          <h3>
            Contact Us
          </h3>


          <p>
            <FaPhoneAlt />
            <a href="tel:+919555620833">
              +91 9555620833
            </a>
          </p>


          <p>
            <FaPhoneAlt />
            <a href="tel:+919958431462">
              +91 9958431462
            </a>
          </p>


          <p>
            <FaEnvelope />
            info@deepufabricator.com
          </p>


          <p>
            <FaMapMarkerAlt />
            Wazirpur Road, Nehar Par,
            Near Sika Gas Agency,
            Faridabad - 121002
          </p>


        </div>


      </div>



      <div className="footer-bottom">

        <p>
          © 2026 Deepu Fabricator. All Rights Reserved.
        </p>

      </div>


    </footer>

  );

}


export default Footer;

