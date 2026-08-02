import React, { useState } from "react";
import CTA from "../components/CTA/CTA";
import ServiceHero from "../components/ServicesPage/ServiceHero";
import ServicesGrid from "../components/ServicesPage/ServicesGrid";
import WorkingProcess from "../components/ServicesPage/WorkingProcess";
import WhyChooseUs from "../components/WhyChooseUs/WhyChooseUs";
import Industries from "../components/ServicesPage/Industries";
import FAQ from "../components/ServicesPage/FAQ";
import QuotationForm from "../components/QuotationForm/QuotationForm";

function Services() {
  const [password, setPassword] = useState("");
  const [isUnlocked, setIsUnlocked] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const ADMIN_PASSWORD = "Deepu@1904";

  const handleLogin = (e) => {
    e.preventDefault();
    if (password === ADMIN_PASSWORD) {
      setIsUnlocked(true);
      setErrorMessage("");
    } else {
      setIsUnlocked(false);
      setErrorMessage("❌ Invalid Password! Please try again.");
      setPassword("");
    }
  };

  return (
    <>
      <ServiceHero />

      <ServicesGrid />

      {/* 📊 पासवर्ड प्रोटेक्टेड कोटेशन कैलकुलेटर सेक्शन */}
      <div style={{ backgroundColor: "#f9f9f9", padding: "50px 0", fontFamily: "Arial, sans-serif" }}>
        <div style={{ maxWidth: "900px", margin: "0 auto", padding: "0 20px" }}>
          
          {!isUnlocked ? (
            <div style={{ 
              maxWidth: "400px", 
              margin: "0 auto", 
              padding: "30px", 
              border: "1px solid #e0e0e0", 
              borderRadius: "12px", 
              boxShadow: "0 4px 15px rgba(0,0,0,0.06)", 
              textAlign: "center",
              backgroundColor: "#ffffff"
            }}>
              <div style={{ fontSize: "40px", marginBottom: "10px" }}>🔒</div>
              <h3 style={{ color: "#2c3e50", margin: "0 0 10px 0" }}>Service Management</h3>
              <p style={{ color: "#7f8c8d", fontSize: "14px", marginBottom: "20px" }}>
                Only authorized admin can access the quotation panel.
              </p>

              <form onSubmit={handleLogin}>
                <div style={{ marginBottom: "15px", textAlign: "left" }}>
                  <label style={{ fontWeight: "bold", fontSize: "14px", color: "#34495e", display: "block", marginBottom: "5px" }}>
                    Enter Password:
                  </label>
                  <input 
                    type="password" 
                    placeholder="••••••••" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    style={{ 
                      width: "100%", 
                      padding: "12px", 
                      boxSizing: "border-box", 
                      borderRadius: "6px", 
                      border: "1px solid #ccc",
                      fontSize: "16px",
                      outline: "none"
                    }}
                    required
                  />
                </div>

                {errorMessage && (
                  <div style={{ 
                    color: "#e74c3c", 
                    backgroundColor: "#fde8e7", 
                    padding: "10px", 
                    borderRadius: "6px", 
                    fontSize: "14px", 
                    marginBottom: "15px",
                    fontWeight: "500"
                  }}>
                    {errorMessage}
                  </div>
                )}

                <button type="submit" style={{ 
                  width: "100%", 
                  padding: "12px", 
                  backgroundColor: "#0d6efd", 
                  color: "white", 
                  border: "none", 
                  borderRadius: "6px", 
                  cursor: "pointer", 
                  fontWeight: "bold",
                  fontSize: "16px"
                }}>
                  Login
                </button>
              </form>
            </div>
          ) : (
            <div>
              <div style={{ textAlign: "right", marginBottom: "15px" }}>
                <button 
                  onClick={() => { setIsUnlocked(false); setErrorMessage(""); }} 
                  style={{ 
                    padding: "8px 16px", 
                    background: "#e74c3c", 
                    color: "white", 
                    border: "none", 
                    borderRadius: "6px", 
                    cursor: "pointer",
                    fontWeight: "bold"
                  }}
                >
                  Logout / Lock Panel
                </button>
              </div>
              <QuotationForm />
            </div>
          )}

        </div>
      </div>

      <WorkingProcess />

      <WhyChooseUs />

      <Industries />

      <FAQ />

      <CTA />
    </>
  );
}

export default Services;


