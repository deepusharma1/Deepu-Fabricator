import "./FAQ.css";
import { useState } from "react";
import { FaPlus, FaMinus } from "react-icons/fa";

const faqData = [
  {
    question: "What fabrication services do you provide?",
    answer:
      "We provide Steel Gates, Rolling Shutters, Hydraulic Scissor Lifts, Industrial Sheds, Railings, Staircases and Custom Fabrication.",
  },
  {
    question: "Do you provide custom fabrication?",
    answer:
      "Yes, every project is customized according to customer requirements and site dimensions.",
  },
  {
    question: "Do you offer installation services?",
    answer:
      "Yes, our experienced team provides complete installation services at your location.",
  },
  {
    question: "How long does a project take?",
    answer:
      "Project duration depends on the design and quantity, but we always aim for timely delivery.",
  },
  {
    question: "Do you use high-quality materials?",
    answer:
      "Yes, we use premium-grade steel and modern fabrication techniques.",
  },
  {
    question: "Can I request a free quotation?",
    answer:
      "Absolutely. Contact us through the website to receive a free estimate.",
  },
];

function FAQ() {
  const [openIndex, setOpenIndex] = useState(null);

  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <section className="faq-section">

      <div className="faq-title">

        <span>FREQUENTLY ASKED QUESTIONS</span>

        <h2>Have Any Questions?</h2>

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
              onClick={() => toggleFAQ(index)}
            >

              <h3>{item.question}</h3>

              {openIndex === index ? <FaMinus /> : <FaPlus />}

            </div>

            {openIndex === index && (
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

