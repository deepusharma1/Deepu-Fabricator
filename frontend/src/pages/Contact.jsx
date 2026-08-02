import CTA from "../components/CTA/CTA";

import ContactHero from "../components/ContactPage/ContactHero";
import ContactForm from "../components/ContactPage/ContactForm";
import BusinessHours from "../components/ContactPage/BusinessHours";
import GoogleMap from "../components/ContactPage/GoogleMap";

function Contact() {
  return (
    <>
      {/* 2. Top Red Action Banner */}
      <ContactHero />

      {/* 3. Modern Material-UI Query Form */}
      <ContactForm />

      {/* 4. Elegant Working Hours Table */}
      <BusinessHours />

      {/* 5. Live Interactive Location Map */}
      <GoogleMap />

      {/* 6. Call To Action */}
      <CTA />
    </>
  );
}

export default Contact;


