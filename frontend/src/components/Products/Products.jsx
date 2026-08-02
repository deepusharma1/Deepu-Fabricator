import "./Products.css";

import gate from "../../assets/products/steel-gate.jpg";
import shutter from "../../assets/products/rolling-shutter.jpg";
import lift from "../../assets/products/hydraulic-scissor-lift.jpg";
import railing from "../../assets/products/ms-railing.jpg";
import staircase from "../../assets/products/steel-staircase.jpg";
import shed from "../../assets/products/industrial-shed.jpg";

const products = [
  {
    title: "Steel Gate",
    image: gate,
  },
  {
    title: "Rolling Shutter",
    image: shutter,
  },
  {
    title: "Hydraulic Scissor Lift",
    image: lift,
  },
  {
    title: "MS Railing",
    image: railing,
  },
  {
    title: "Steel Staircase",
    image: staircase,
  },
  {
    title: "Industrial Shed",
    image: shed,
  },
];

function Products() {
  return (
    <section className="products">
      <div className="container">
        <div className="section-header">
          <span className="section-subtitle">OUR PRODUCTS</span>
          <h2 className="section-title">Premium Fabrication Products</h2>
          <p className="section-desc">
            We manufacture premium quality fabrication products for
            industrial, commercial and residential projects.
          </p>
        </div>

        <div className="products-grid">
          {products.map((item, index) => (
            <div className="product-card" key={index}>
              <div className="product-img">
                <img src={item.image} alt={item.title} />
              </div>
              <div className="product-content">
                <h3>{item.title}</h3>
                <button className="product-btn">View Details</button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Products;

