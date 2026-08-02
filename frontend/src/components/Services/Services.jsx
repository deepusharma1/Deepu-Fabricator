import { useState } from "react";
import "./Services.css";

import {
  FaIndustry,
  FaTools,
  FaWarehouse,
  FaTruckMoving,
  FaHardHat,
  FaCogs,
  FaLock,
  FaFileInvoiceDollar
} from "react-icons/fa";


const services = [
  {
    icon: <FaIndustry />,
    title: "Steel Fabrication",
    description:
      "Complete industrial and commercial steel fabrication using high quality materials with durable finishing."
  },

  {
    icon: <FaTools />,
    title: "Professional Welding",
    description:
      "MIG, TIG and Arc welding solutions with strong joints and accurate fabrication work."
  },

  {
    icon: <FaWarehouse />,
    title: "Rolling Shutter",
    description:
      "Heavy duty rolling shutter manufacturing, installation and maintenance for industrial requirements."
  },

  {
    icon: <FaTruckMoving />,
    title: "Hydraulic Crane Work",
    description:
      "Custom hydraulic crane fabrication and maintenance solutions for heavy load applications."
  },

  {
    icon: <FaHardHat />,
    title: "Hydraulic Scissor Lift",
    description:
      "Safe and reliable industrial lifting platforms designed according to project requirements."
  },

  {
    icon: <FaCogs />,
    title: "Custom Metal Fabrication",
    description:
      "Customized gates, railings, sheds and structural fabrication solutions."
  }
];


function Services() {

  const [showLogin,setShowLogin] = useState(false);
  const [password,setPassword] = useState("");
  const [isAdmin,setIsAdmin] = useState(false);


  const handleLogin = () => {

    const adminPassword = "deepu123";

    if(password === adminPassword){

      setIsAdmin(true);
      setShowLogin(false);

    }
    else{

      alert(typeof "Invalid Password" === "object" ? JSON.stringify("Invalid Password") : "Invalid Password");

    }

  };


  return (

<section className="services">

<div className="container">


{/* Header */}

<div className="section-header">

<span className="section-subtitle">
OUR SERVICES
</span>


<h2 className="section-title">
Professional Fabrication Solutions
</h2>


<p className="section-desc">

We provide complete fabrication services including
steel gates, rolling shutters, industrial sheds,
hydraulic lifts and customized metal structures.

</p>


</div>




{/* Services Cards */}

<div className="service-grid">


{
services.map((service,index)=>(


<div className="service-card" key={index}>


<div className="service-icon">

{service.icon}

</div>



<h3>
{service.title}
</h3>



<p>
{service.description}
</p>



<button className="service-btn">
Get Quote
</button>



</div>


))
}



</div>





{/* Quotation Lock Section */}


<div className="quotation-lock">


{

!isAdmin ?


<>


<FaLock className="lock-icon"/>


<h3>
Service Management
</h3>


<p>
Authorized admin access required for quotation management.
</p>



{

showLogin &&

<div className="login-box">


<input

type="password"

placeholder="Enter Password"

value={password}

onChange={(e)=>setPassword(e.target.value)}

/>



<button onClick={handleLogin}>
Login
</button>


</div>


}





{

!showLogin &&

<button

className="admin-btn"

onClick={()=>setShowLogin(true)}

>

Open Quotation Panel

</button>


}


</>


:


<div className="quotation-panel">


<FaFileInvoiceDollar className="quote-icon"/>


<h3>
Quotation Management
</h3>


<p>
Admin access granted. Create professional customer quotations.
</p>


<button className="admin-btn">

Create Quotation

</button>



</div>


}



</div>



</div>

</section>

  );

}


export default Services;

