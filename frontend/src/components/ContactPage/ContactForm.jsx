import API from "../../api/axios";
import React, { useState } from "react";

import {
  Box,
  TextField,
  Button,
  Typography,
  Card,
  CardContent,
  Grid,
  MenuItem
} from "@mui/material";


const workTypes = [
  {
    value: "Steel Gate / Grill",
    label: "Steel Gate / Grill Work"
  },
  {
    value: "Rolling Shutter",
    label: "Rolling Shutter Installation"
  },
  {
    value: "Hydraulic Scissor Lift",
    label: "Hydraulic Scissor Lift"
  },
  {
    value: "Industrial Shed",
    label: "Industrial Shed Construction"
  },
  {
    value: "Other Fabrication",
    label: "Other Fabrication Work"
  }
];


function ContactForm(){

const [formData,setFormData] = useState({

  fullName:"",
  mobileNumber:"",
  emailAddress:"",
  requirementType:"Steel Gate / Grill",
  message:""

});


const [isSubmitting,setIsSubmitting] = useState(false);



const handleChange = (e)=>{

setFormData({

...formData,

[e.target.name]:e.target.value

});

};




const handleSubmit = async(e)=>{

e.preventDefault();

setIsSubmitting(true);


try{


const response = await API.post("/contact/", formData);


const data = response.data;



if(response.status === 200 || response.status === 201){


alert(
"Your inquiry has been submitted successfully. Our team will contact you soon."
);



setFormData({

fullName:"",
mobileNumber:"",
emailAddress:"",
requirementType:"Steel Gate / Grill",
message:""

});


}

else{


alert(typeof "Something went wrong" === "object" ? JSON.stringify("Something went wrong") : "Something went wrong");


}


}

catch(error){


console.error(
"Contact API Error:",
error.response?.data || error.message
);



alert(

error.response?.data?.detail ||

"Server connection failed. Please start backend."

);


}



finally{


setIsSubmitting(false);


}


};




return(

<Box

component="section"

sx={{

width:"100%",

py:{
xs:3,
sm:5,
md:8
},

px:{
xs:1.5,
sm:3
},

display:"flex",

justifyContent:"center",

overflow:"hidden"

}}

>


<Card

sx={{

width:"100%",

maxWidth:"850px",

borderRadius:{
xs:2,
md:4
},

boxShadow:
"0 10px 30px rgba(0,0,0,0.12)"

}}

>


<CardContent

sx={{

p:{
xs:2,
sm:4,
md:5
}

}}

>


<Typography

variant="h4"

textAlign="center"

fontWeight="800"

sx={{

fontSize:{
xs:"1.4rem",
sm:"1.8rem",
md:"2rem"
},

mb:1

}}

>

Send Us A Message

</Typography>



<Typography

textAlign="center"

color="text.secondary"

sx={{

mb:4,

fontSize:{
xs:"0.85rem",
sm:"1rem"
}

}}

>

Fill out the form below and our team will contact you.

</Typography>



<form onSubmit={handleSubmit}>


<Grid container spacing={{xs:2,sm:3}}>


<Grid item xs={12} sm={6}>

<TextField

fullWidth

label="Full Name"

name="fullName"

value={formData.fullName}

onChange={handleChange}

required

/>

</Grid>



<Grid item xs={12} sm={6}>

<TextField

fullWidth

label="Mobile Number"

name="mobileNumber"

value={formData.mobileNumber}

onChange={handleChange}

required

inputProps={{

maxLength:10

}}

/>

</Grid>



<Grid item xs={12}>


<TextField

fullWidth

label="Email Address"

name="emailAddress"

type="email"

value={formData.emailAddress}

onChange={handleChange}

/>


</Grid>




<Grid item xs={12}>


<TextField

fullWidth

select

label="Requirement Type"

name="requirementType"

value={formData.requirementType}

onChange={handleChange}

required

>


{

workTypes.map((item)=>(

<MenuItem

key={item.value}

value={item.value}

>

{item.label}

</MenuItem>

))

}


</TextField>


</Grid>




<Grid item xs={12}>


<TextField

fullWidth

label="Message"

name="message"

multiline

rows={5}

value={formData.message}

onChange={handleChange}

required

placeholder="Describe your requirement..."

/>


</Grid>




<Grid item xs={12}>


<Button

fullWidth

type="submit"

variant="contained"

disabled={isSubmitting}

sx={{

py:1.5,

borderRadius:2,

fontWeight:700,

background:"#ff3b3b",

fontSize:{
xs:"0.9rem",
sm:"1rem"
},

"&:hover":{

background:"#d62828"

}

}}

>


{

isSubmitting

?

"Sending..."

:

"Submit Requirement"

}


</Button>


</Grid>


</Grid>


</form>


</CardContent>


</Card>


</Box>


);

}


export default ContactForm;



