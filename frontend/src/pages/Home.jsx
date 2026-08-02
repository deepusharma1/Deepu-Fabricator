import React, { Suspense, lazy } from "react";

import Hero from "../components/Hero/Hero";
import Services from "../components/Services/Services";
import About from "../components/About/About";
import Preloader from "../components/Preloader/Preloader";

import CTA from "../components/CTA/CTA";
import WhyChooseUs from "../components/WhyChooseUs/WhyChooseUs";


// Lazy loaded components

const Projects = lazy(() =>
  import("../components/Projects/Projects")
);

const Counter = lazy(() =>
  import("../components/Counter/Counter")
);

const Process = lazy(() =>
  import("../components/Process/Process")
);

const Products = lazy(() =>
  import("../components/Products/Products")
);

const Testimonials = lazy(() =>
  import("../components/Testimonials/Testimonials")
);

const Industries = lazy(() =>
  import("../components/Industries/Industries")
);

const FAQ = lazy(() =>
  import("../components/FAQ/FAQ")
);

const LiveInbox = lazy(() =>
  import("../components/InboxPage/LiveInbox")
);


function Home() {

  return (
    <>

      <Hero />

      <Services />

      <About />


      <Suspense fallback={<Preloader />}>

        <WhyChooseUs />

        <Projects />

        <Counter />

        <Process />

        <Products />

        <Testimonials />

        <Industries />

        <FAQ />

        <CTA />

        <LiveInbox />

      </Suspense>


    </>
  );
}


export default Home;

