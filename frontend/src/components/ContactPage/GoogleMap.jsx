import React from "react";
import "./GoogleMap.css";

function GoogleMap() {
  const directionUrl = "https://google.com";

  return (
    <div className="map-section">
      <h2 className="map-title">Find Us On Google Maps</h2>
      <p className="map-subtitle">Visit our workshop for custom steel and fabrication requirements</p>

      <div className="map-card-container">
        <div className="map-visual-placeholder">
          <div className="map-overlay-content">
            <span style={{ fontSize: "3rem" }}>📍</span>
            <h3>Deepu Fabricator Workshop</h3>
            <p>Sector 87, Neharpar Faridabad, Haryana</p>
            
            <a 
              href={directionUrl} 
              target="_blank" 
              rel="noopener noreferrer" 
              className="track-route-btn-card"
            >
              Open Live Route Tracking
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default GoogleMap;


