import React, { useState, useEffect } from "react";
import API from "../../api/axios";

import {
  Box,
  Typography,
  Paper,
  Divider,
  Button,
  CircularProgress,
  Badge,
  TextField,
  Card,
  CardContent
} from "@mui/material";

import "./LiveInbox.css";


function LiveInbox() {


  const [isAuthenticated,setIsAuthenticated] = useState(false);

  const [loginData,setLoginData] = useState({
    username:"",
    password:""
  });


  const [loginError,setLoginError] = useState("");

  const [isLoggingIn,setIsLoggingIn] = useState(false);


  const [messages,setMessages] = useState([]);

  const [selectedMsg,setSelectedMsg] = useState(null);

  const [loading,setLoading] = useState(false);



  // =====================================================
  // CHECK EXISTING LOGIN TOKEN
  // =====================================================

  useEffect(()=>{


    const token = localStorage.getItem("token");


    if(token){

      setIsAuthenticated(true);

    }


  },[]);





  // =====================================================
  // FETCH ADMIN INBOX
  // =====================================================

  const fetchInboxMessages = async()=>{


    setLoading(true);


    try{


      const response = await API.get(
        "/admin/queries"
      );


      console.log(
        "INBOX RESPONSE:",
        response.data
      );



      const inboxData =
      response.data.data || [];



      setMessages(
        inboxData
      );



      if(inboxData.length > 0){

        setSelectedMsg(
          inboxData[0]
        );

      }
      else{

        setSelectedMsg(null);

      }


    }
    catch(error){


      console.error(
        "FETCH INBOX ERROR:",
        error.response?.data || error.message
      );



      if(error.response?.status===401){


        localStorage.removeItem(
          "token"
        );


        localStorage.removeItem(
          "refresh_token"
        );


        setIsAuthenticated(false);


      }


    }
    finally{

      setLoading(false);

    }


  };






  useEffect(()=>{


    if(isAuthenticated){

      fetchInboxMessages();

    }


  },[isAuthenticated]);






  // =====================================================
  // LOGIN INPUT CHANGE
  // =====================================================


  const handleLoginChange=(e)=>{


    setLoginData({

      ...loginData,

      [e.target.name]:
      e.target.value

    });


    setLoginError("");

  };






  // =====================================================
  // ADMIN LOGIN
  // =====================================================


  const handleAdminLoginSubmit = async(e)=>{


    e.preventDefault();


    setIsLoggingIn(true);


    try{


      const response = await API.post(

        "/auth/login",

        loginData

      );



      console.log(
        "LOGIN RESPONSE:",
        response.data
      );



      const data=response.data;



      if(
        response.status===200 &&
        data.access_token
      ){


        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("token", data.access_token);



        if(data.refresh_token){


          localStorage.setItem(

            "refresh_token",

            data.refresh_token

          );


        }



        setIsAuthenticated(true);


        setLoginError("");

      }
      else{


        setLoginError(
          "Invalid username or password"
        );


      }



    }
    catch(error){


      console.error(

        "LOGIN ERROR:",

        error.response?.data || error.message

      );


      setLoginError(

        error.response?.data?.detail ||

        "Login Failed"

      );


    }
    finally{


      setIsLoggingIn(false);


    }


  };
// =====================================================
// DELETE QUERY
// =====================================================

const handleDeleteQuery = async(id)=>{


  const confirmDelete = window.confirm(
    "Delete this inquiry?"
  );


  if(!confirmDelete)
    return;



  try{


    const response = await API.delete(

      `/admin/delete-query/${id}`

    );



    console.log(

      "DELETE RESPONSE:",

      response.data

    );



    if(response.status===200){


      setMessages(

        previous =>

        previous.filter(

          item => item.id !== id

        )

      );



      setSelectedMsg(null);



      alert(

        "Inquiry deleted successfully"

      );


    }



  }
  catch(error){


    console.error(

      "DELETE ERROR:",

      error.response?.data || error.message

    );



    if(error.response?.status===401){


      logoutAdmin();


    }
    else{


      alert(

        "Delete failed"

      );


    }


  }


};







// =====================================================
// DOWNLOAD BACKUP CSV
// =====================================================

const handleDownloadBackup = async()=>{


  try{


    const response = await API.get(

      "/admin/download-backup",

      {

        responseType:"blob"

      }

    );



    const blob = new Blob(

      [

        response.data

      ],

      {

        type:"text/csv"

      }

    );



    const url = window.URL.createObjectURL(

      blob

    );



    const link=document.createElement(

      "a"

    );



    link.href=url;



    link.download =

    `Deepu_Fabricator_Backup_${Date.now()}.csv`;



    document.body.appendChild(

      link

    );



    link.click();



    link.remove();



    window.URL.revokeObjectURL(

      url

    );



  }
  catch(error){


    console.error(

      "BACKUP DOWNLOAD ERROR:",

      error.response?.data || error.message

    );



    if(error.response?.status===401){


      logoutAdmin();


    }
    else{


      alert(

        "Backup download failed"

      );


    }


  }


};







// =====================================================
// LOGOUT ADMIN
// =====================================================

const logoutAdmin = ()=>{


  localStorage.removeItem(

    "token"

  );


  localStorage.removeItem(

    "refresh_token"

  );


  setIsAuthenticated(false);


  setMessages([]);


  setSelectedMsg(null);


};





// =====================================================
// SHOW LOADING
// =====================================================

if(loading){


  return(

    <Box

      sx={{

        textAlign:"center",

        py:5

      }}

    >


      <CircularProgress />


      <Typography

        sx={{

          mt:2

        }}

      >

        Loading Inbox...

      </Typography>


    </Box>

  );


}

// =====================================================
// LOGIN SCREEN
// =====================================================

if(!isAuthenticated){


return (

<Box

sx={{

display:"flex",

justifyContent:"center",

py:8,

px:2,

background:"#fafafa",

minHeight:"70vh"

}}

>


<Card

sx={{

width:"100%",

maxWidth:"420px",

borderRadius:3,

boxShadow:"0 8px 30px rgba(0,0,0,0.12)"

}}

>


<CardContent

sx={{

p:4,

textAlign:"center"

}}

>


<Typography

variant="h5"

fontWeight="bold"

>

🔐 Admin Security Access

</Typography>



<Typography

variant="body2"

color="textSecondary"

sx={{

mt:1,

mb:3

}}

>

Enter admin credentials to access inquiry inbox.

</Typography>





<form

onSubmit={handleAdminLoginSubmit}

>



<TextField


fullWidth


label="Admin Username"


name="username"


value={loginData.username}


onChange={handleLoginChange}


margin="normal"


required


/>



<TextField


fullWidth


type="password"


label="Admin Password"


name="password"


value={loginData.password}


onChange={handleLoginChange}


margin="normal"


required


/>



{

loginError &&


<Typography

color="error"

sx={{

mt:1

}}

>

{loginError}

</Typography>


}





<Button


fullWidth


type="submit"


variant="contained"


disabled={isLoggingIn}


sx={{

mt:3,

py:1.5,

background:"#d32f2f",

"&:hover":{

background:"#b71c1c"

}

}}


>


{

isLoggingIn

?

"Authorizing..."

:

"Open Inbox"

}



</Button>



</form>



</CardContent>


</Card>


</Box>


);


}


// =====================================================
// MAIN INBOX UI
// =====================================================


return (

<Box

className="master-inbox-section"

sx={{

p:2

}}

>



{/* HEADER */}

<Box

sx={{

display:"flex",

justifyContent:"space-between",

alignItems:"center",

mb:3,

flexWrap:"wrap",

gap:2

}}

>



<Typography

variant="h5"

fontWeight="bold"

>

📥 Customer Inquiry Inbox


<Badge

badgeContent={messages.length}

color="error"

sx={{

ml:3

}}

/>


</Typography>





<Box

sx={{

display:"flex",

gap:2

}}

>


<Button


variant="contained"


onClick={handleDownloadBackup}


sx={{

background:"#222"

}}


>

📥 Download Backup

</Button>




<Button


variant="outlined"


onClick={fetchInboxMessages}

>

🔄 Refresh

</Button>



<Button


variant="outlined"


color="error"


onClick={logoutAdmin}

>

Logout

</Button>



</Box>



</Box>









<Box

className="inbox-split-container"

sx={{

display:"flex",

gap:2

}}

>



{/* LEFT MESSAGE LIST */}


<Box

className="inbox-sidebar-list"

sx={{

width:"35%"

}}

>



{

messages.length===0


?


<Typography

sx={{

p:3,

color:"#777"

}}

>

No inquiries found.

</Typography>


:


messages.map((msg)=>(


<Box


key={msg.id}


onClick={()=>setSelectedMsg(msg)}


className={

selectedMsg?.id===msg.id

?

"inbox-mail-card active-mail"

:

"inbox-mail-card"

}


sx={{

cursor:"pointer",

p:2,

mb:1

}}


>


<Typography

fontWeight="bold"

>

{msg.full_name || msg.name || msg.customer_name || "Customer"}

</Typography>



<Typography

variant="caption"

>

{msg.requirement_type}

</Typography>



<Typography

variant="body2"

noWrap

>

{msg.message}

</Typography>



</Box>


))


}



</Box>









{/* RIGHT DETAIL VIEW */}


<Box

component={Paper}

className="inbox-mail-body-view"

sx={{

width:"65%",

p:3

}}

>



{

selectedMsg


?


<>


<Typography

variant="h6"

fontWeight="bold"

>

{selectedMsg.requirement_type}

Job Request

</Typography>




<Divider

sx={{

my:2

}}

/>





<Typography>

<b>From:</b>{" "}

{selectedMsg.full_name || selectedMsg.name || selectedMsg.customer_name}

</Typography>




<Typography>

<b>Email:</b>{" "}

{

selectedMsg.email_address || selectedMsg.emailAddress || selectedMsg.email ||

"No Email"

}

</Typography>




<Typography>

<b>Mobile:</b>{" "}

{selectedMsg.mobile_number || selectedMsg.mobileNumber || selectedMsg.mobile}

</Typography>





<Typography

variant="caption"

>


Received:


{" "}


{

new Date(

selectedMsg.created_at

)

.toLocaleString("en-IN")

}


</Typography>





<Divider

sx={{

my:2

}}

/>





<Typography

fontWeight="bold"

>

Inquiry Message:

</Typography>




<Typography

sx={{

mt:1

}}

>

{selectedMsg.message}

</Typography>








<Box

sx={{

mt:4,

display:"flex",

gap:2

}}

>



<Button


variant="contained"


component="a"


href={

`tel:${selectedMsg.mobile_number || selectedMsg.mobileNumber || selectedMsg.mobile}`

}


>

📞 Call Customer

</Button>






<Button


variant="outlined"


color="error"


onClick={()=>handleDeleteQuery(selectedMsg.id)}

>

🗑️ Delete Inquiry

</Button>



</Box>



</>


:


<Typography

sx={{

textAlign:"center",

mt:5

}}

>

Select inquiry

</Typography>



}



</Box>



</Box>



</Box>


);


}


export default LiveInbox;









