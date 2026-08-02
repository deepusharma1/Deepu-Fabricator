import "./ContactHero.css";
import { Link } from "react-router-dom";
import { FaPhoneAlt } from "react-icons/fa";


function ContactHero() {


return (

<section className="contact-hero">


<div className="contact-overlay">


<div className="contact-content">


<span>
CONTACT US
</span>



<h1>
Let's Build Something Great Together
</h1>




<p>
Contact Deepu Fabricator for Steel Gates,
Rolling Shutters, Hydraulic Scissor Lifts,
Industrial Sheds and complete fabrication work.
</p>





<div className="contact-buttons">



<Link 
to="/services"
className="contact-btn"
>

Our Services

</Link>





<a
href="tel:+919555620833"
className="contact-btn-outline"
>

<FaPhoneAlt />

&nbsp;

+91 95556 20833

</a>





<a
href="tel:+919958431462"
className="contact-btn-outline"
>

<FaPhoneAlt />

&nbsp;

+91 99584 31462

</a>





</div>



</div>


</div>


</section>

);


}


export default ContactHero;

