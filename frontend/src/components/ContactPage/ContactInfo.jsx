import React from "react";

import {
  Grid,
  Card,
  CardContent,
  Typography,
  Box
} from "@mui/material";

import {
  LocationOn,
  Email,
  Phone,
  AccessTime
} from "@mui/icons-material";

import "./ContactInfo.css";


const contactData = [

{
title:"Address",
icon:<LocationOn fontSize="large"/>,
details:
"Wazirpur Road, Nehar Par,\nNear Sika Gas Agency,\nFaridabad - 121002"
},


{
title:"Email",
icon:<Email fontSize="large"/>,
details:"info@deepufabricator.com"
},


{
title:"Phone",
icon:<Phone fontSize="large"/>,
details:
"+91 9555620833\n+91 9958431462"
},


{
title:"Working Hours",
icon:<AccessTime fontSize="large"/>,
details:
"Monday - Saturday\n9:00 AM - 6:00 PM"
}


];





function ContactInfo(){


return(


<section className="contact-info-container">


<Grid

container

spacing={3}

justifyContent="center"

maxWidth="1200px"

>


{

contactData.map((item,index)=>(


<Grid

item

xs={12}

sm={6}

md={3}

key={index}

>


<Card className="contact-card">


<CardContent>


<Box className="contact-icon">

{item.icon}

</Box>




<Typography

className="contact-title"

variant="h6"

>

{item.title}

</Typography>





<Typography

className="contact-details"

>

{item.details}

</Typography>



</CardContent>



</Card>


</Grid>


))

}



</Grid>



</section>


);


}


export default ContactInfo;

