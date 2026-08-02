import { Routes, Route } from "react-router-dom";

import Home from "../pages/Home";
import About from "../pages/About";
import Services from "../pages/Services";
import Gallery from "../pages/Gallery";
import OrderNow from "../pages/OrderNow";
import RequestQuote from "../pages/RequestQuote";
import TrackOrder from "../pages/TrackOrder";
import Contact from "../pages/Contact";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Inbox from "../pages/Inbox";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/services" element={<Services />} />
      <Route path="/gallery" element={<Gallery />} />
      <Route path="/order" element={<OrderNow />} />
      <Route path="/quote" element={<RequestQuote />} />
      <Route path="/track" element={<TrackOrder />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/inbox" element={<Inbox />} />
    </Routes>
  );
}

