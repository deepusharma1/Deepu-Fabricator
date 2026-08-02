import React from 'react';
import './PageTitle.css';

const PageTitle = ({ title, parentPage = "Home" }) => {
  return (
    <div className="page-title-banner">
      <div className="page-title-content">
        <h1>{title}</h1>
        <div className="breadcrumb">
          <span>{parentPage}</span>
          <span className="separator">/</span>
          <span className="current-page">{title}</span>
        </div>
      </div>
    </div>
  );
};

export default PageTitle;


