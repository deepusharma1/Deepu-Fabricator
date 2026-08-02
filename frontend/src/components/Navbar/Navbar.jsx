import React, { useState, useEffect } from "react";
import { Link, NavLink, useLocation } from "react-router-dom";
import { FaPhoneAlt, FaBars, FaTimes } from "react-icons/fa";
import "./Navbar.css";


function Navbar() {

  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  const location = useLocation();


  const navItems = [
    {
      name:"Home",
      path:"/"
    },
    {
      name:"About",
      path:"/about"
    },
    {
      name:"Services",
      path:"/services"
    },
    {
      name:"Gallery",
      path:"/gallery"
    },
    {
      name:"Contact",
      path:"/contact"
    }
  ];



  // Close mobile menu after route change
  useEffect(()=>{

    setIsOpen(false);

  },[location]);



  // Body scroll lock
  useEffect(()=>{

    if(isOpen){

      document.body.classList.add("nav-open");

    }
    else{

      document.body.classList.remove("nav-open");

    }


    return ()=>{

      document.body.classList.remove("nav-open");

    };


  },[isOpen]);




  // Navbar shadow on scroll

  useEffect(()=>{


    const handleScroll=()=>{

      setScrolled(window.scrollY > 50);

    };


    window.addEventListener(
      "scroll",
      handleScroll
    );


    return()=>{

      window.removeEventListener(
        "scroll",
        handleScroll
      );

    };


  },[]);




  return (

    <header className={`navbar ${scrolled ? "scrolled":""}`}>


      {/* Overlay */}

      <div
        className={`nav-overlay ${isOpen ? "show":""}`}
        onClick={()=>setIsOpen(false)}
      />



      <div className="container nav-container">



        {/* Logo */}

        <div className="logo">

          <Link to="/">

            <span>Deepu</span> Fabricator

          </Link>

        </div>





        {/* Menu */}

        <nav className={`nav-menu ${isOpen ? "active":""}`}>


          <ul className="nav-links">


            {
              navItems.map((item)=>(

                <li key={item.path}>

                  <NavLink
                    to={item.path}
                    className={({isActive})=>
                      isActive ? "active":""
                    }
                  >

                    {item.name}

                  </NavLink>

                </li>


              ))
            }


          </ul>




          {/* Mobile Contact */}

          <div className="mobile-phone-list">


            <a href="tel:+919555620833">

              <FaPhoneAlt/>

              +91 9555620833

            </a>



            <a href="tel:+919958431462">

              <FaPhoneAlt/>

              +91 9958431462

            </a>


          </div>



        </nav>





        {/* Desktop Call */}


        <div className="call-btn-wrapper">


          <div className="call-btn">


            <FaPhoneAlt/>


            <div className="phone-list">


              <a href="tel:+919555620833">

                +91 9555620833

              </a>


              <a href="tel:+919958431462">

                +91 9958431462

              </a>


            </div>


          </div>


        </div>






        {/* Mobile Button */}


        <button

          type="button"

          className="hamburger"

          onClick={()=>setIsOpen(!isOpen)}

          aria-label="menu"

        >

          {
            isOpen
            ?
            <FaTimes/>
            :
            <FaBars/>
          }


        </button>



      </div>


    </header>

  );

}


export default Navbar;

