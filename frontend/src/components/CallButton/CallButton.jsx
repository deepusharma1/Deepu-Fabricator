import React from "react";
import "./CallButton.css";

const CallButton = () => {
  return (
    <a
      href="tel:+919555620833"
      className="call-float"
      aria-label="Call Deepu Fabricator"
    >
      <span className="call-icon">
        📞
      </span>
    </a>
  );
};

export default CallButton;

