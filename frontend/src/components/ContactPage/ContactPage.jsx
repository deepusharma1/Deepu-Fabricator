import React from "react";

import {
  Box,
  Typography,
  Divider
} from "@mui/material";

import ContactInfo from "./ContactInfo";
import ContactForm from "./ContactForm";
import GoogleMap from "./GoogleMap";



function ContactPage(){


return(


<Box

sx={{

width:"100%",

minHeight:"100vh",

backgroundColor:"#f8f9fa",

overflow:"hidden",

py:{
xs:3,
sm:5,
md:6
}

}}

>





<Box

sx={{

textAlign:"center",

px:{
xs:2,
sm:3
},

mb:{
xs:3,
md:5
}

}}

>



<Typography

variant="h3"

fontWeight="800"

sx={{

fontSize:{
xs:"2rem",
sm:"2.5rem",
md:"3rem"
},

mb:2,

color:"#111827"

}}

>

Contact Us

</Typography>





<Typography

variant="body1"

color="text.secondary"

sx={{

fontSize:{
xs:"0.9rem",
sm:"1rem"
},

maxWidth:"700px",

mx:"auto"

}}

>

Get in touch with Deepu Fabricator.
We are always ready to help you.

</Typography>



</Box>







<ContactInfo />





<Divider

sx={{

my:{
xs:3,
sm:5
}

}}

/>







<ContactForm />






<Divider

sx={{

my:{
xs:3,
sm:5
}

}}

/>






<GoogleMap />






</Box>


);


}


export default ContactPage;

