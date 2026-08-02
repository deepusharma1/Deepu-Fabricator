import React from "react";
import "./Hero.css";
import { FaPhoneAlt, FaWhatsapp } from "react-icons/fa";


function Hero() {


  const handleScrollToQuote = () => {

    const quoteSection = document.getElementById(
      "quote-form-section"
    );

    if(quoteSection){

      quoteSection.scrollIntoView({
        behavior:"smooth"
      });

    }

  };



  return (

    <section className="hero">


      <div className="hero-overlay">


        <div className="container">


          <div className="hero-content">



            <span className="hero-tag">

              ★ Professional Fabrication Services

            </span>





            <h1>

              DEEPU <span>FABRICATOR</span>

            </h1>





            <h2>

              Rolling Mill • Aluminium Furnace • Steel Fabrication

            </h2>





            <p>

              We provide premium fabrication solutions including
              Hydraulic Crane, Scissor Lift, Rolling Shutter,
              Steel Gates, Aluminium Fabrication,
              Welding Works and Industrial Metal Structures.

            </p>





            <div className="hero-buttons">



              <button

                type="button"

                className="quote-btn"

                onClick={handleScrollToQuote}

              >

                Get Free Quote

              </button>






              <a

                href="https://wa.me/919958431462"

                target="_blank"

                rel="noopener noreferrer"

                className="whatsapp-btn"

              >

                <FaWhatsapp/>

                WhatsApp

              </a>






              <a

                href="tel:+919958431462"

                className="call-btn-hero"

              >

                <FaPhoneAlt/>

                Call Now

              </a>




            </div>







            <div className="hero-counter">



              <div>

                <h3>20+</h3>

                <p>Years Experience</p>

              </div>





              <div>

                <h3>1000+</h3>

                <p>Projects</p>

              </div>





              <div>

                <h3>900+</h3>

                <p>Happy Clients</p>

              </div>



            </div>





          </div>


        </div>


      </div>


    </section>

  );

}


export default Hero;

