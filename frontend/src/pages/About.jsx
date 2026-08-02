import AboutHero from "../components/AboutPage/AboutHero";
import CTA from "../components/CTA/CTA";
import CompanyStory from "../components/AboutPage/CompanyStory";
import MissionVision from "../components/AboutPage/MissionVision";
import Team from "../components/AboutPage/Team";
import WhyChooseAbout from "../components/AboutPage/WhyChooseAbout";
import Certificates from "../components/AboutPage/Certificates";

function About() {
  return (
    <>
      <AboutHero />
      <CompanyStory/>
      <MissionVision />
      <WhyChooseAbout />
      <Team />
      <Certificates />
      <CTA />
    </>
  );
}

export default About;

