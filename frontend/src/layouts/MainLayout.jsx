import React from "react";
import { Outlet } from "react-router-dom";

import Navbar from "../components/Navbar/Navbar";
import Footer from "../components/Footer/Footer";


function MainLayout() {

  return (
    <>

      {/* Navbar */}
      <Navbar />


      {/* Page Content */}
      <main>
        <Outlet />
      </main>


      {/* Footer */}
      <Footer />

    </>
  );
}


export default MainLayout;

