import "./FAQ.css";
import { useState } from "react";
import { FaPlus, FaMinus } from "react-icons/fa";

const faqData = [
  {
    question: "What fabrication services do you provide?",
    answer:
      "We provide steel fabrication, rolling shutters, gates, railings, industrial sheds, staircases, hydraulic scissor lifts, cranes and custom fabrication solutions.",
  },
  {
    question: "Do you provide installation services?",
    answer:
      "Yes, our experienced team provides complete delivery and installation services across various project locations.",
  },
  {
    question: "Can you manufacture custom designs?",
    answer:
      "Absolutely! We manufacture products according to customer drawings, dimensions and specific requirements.",
  },
  {
    question: "Which materials do you use?",
    answer:
      "We use high-quality Mild Steel (MS), Stainless Steel (SS), Aluminium and other premium-grade materials depending on project requirements.",
  },
  {
    question: "How can I request a quotation?",
    answer:
      "You can contact us through our Contact page, phone number or WhatsApp to receive a free quotation.",
  },
];

function FAQ() {
  const [active, setActive] = useState(null);

  const toggle = (index) => {
    setActive(active === index ? null : index);
  };

  return (
    <section className="faq">

      <div className="faq-title">
        <span>FAQ</span>

        <h2>Frequently Asked Questions</h2>

        <p>
          Find answers to the most common questions about our fabrication
          services.
        </p>
      </div>

      <div className="faq-container">

        {faqData.map((item, index) => (

          <div className="faq-item" key={index}>

            <div
              className="faq-question"
              onClick={() => toggle(index)}
            >
              <h3>{item.question}</h3>

              {active === index ? <FaMinus /> : <FaPlus />}
            </div>

            {active === index && (
              <div className="faq-answer">
                <p>{item.answer}</p>
              </div>
            )}

          </div>

        ))}

      </div>

    </section>
  );
}

export default FAQ;

