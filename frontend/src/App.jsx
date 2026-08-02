import React, { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

// Pages
import Home from "./pages/Home";
import About from "./pages/About";
import Services from "./pages/Services";
import Gallery from "./pages/Gallery";
import Contact from "./pages/Contact";

// Components
import Preloader from "./components/Preloader/Preloader";
import ScrollToTop from "./components/RouteScroll/ScrollToTop";
import ScrollTop from "./components/ScrollTop/ScrollTop";
import WhatsApp from "./components/WhatsApp/WhatsApp";
import CallButton from "./components/CallButton/CallButton";
import NotFound from "./components/NotFound/NotFound";


function App() {

  const [loading, setLoading] = useState(true);


  useEffect(() => {

    const timer = setTimeout(() => {
      setLoading(false);
    }, 1500);


    return () => clearTimeout(timer);

  }, []);



  return (

    <>

      {/* Website Loader */}
      {loading && <Preloader />}


      {/* Route Change Scroll Top */}
      <ScrollToTop />


      <Routes>


        {/* Main Website Layout */}
        <Route element={<MainLayout />}>


          <Route 
            path="/" 
            element={<Home />} 
          />


          <Route 
            path="/about" 
            element={<About />} 
          />


          <Route 
            path="/services" 
            element={<Services />} 
          />


          <Route 
            path="/gallery" 
            element={<Gallery />} 
          />


          <Route 
            path="/contact" 
            element={<Contact />} 
          />


        </Route>



        {/* 404 Page */}
        <Route 
          path="*" 
          element={<NotFound />} 
        />


      </Routes>



      {/* Floating Actions */}

      <ScrollTop />

      <WhatsApp />

      <CallButton />


    </>

  );

}


export default App;

