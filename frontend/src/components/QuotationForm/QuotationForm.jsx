import React, {
    useState,
    useEffect
} from "react";

import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

import API from "../../api/axios";

import QuotationItem from "./QuotationItems";

import "./Quotation.css";



const Quotation = () => {



const [quotationName,setQuotationName] = useState(
    "Deepu_Fabricator_Quotation_01"
);



const [formData,setFormData] = useState({

    customerName:"",

    companyName:"DEEPU FABRICATOR",

    mobileNumber:"",

    email:"",

    address:"",

    workType:"Steel Gate / Grill",

    materialType:"Steel",

    leadSource:"Website",


    labourCost:0,

    installationCost:0,

    transportCost:0,

    otherCharges:0,


    gstPercent:18,

    discount:0,


    paymentTerms:"50% Advance Payment",

    deliveryTime:"15-20 Days",

    notes:""

});





const [items,setItems] = useState([

{

    materialName:"",

    description:"",

    quantity:1,

    unit:"Nos",

    rate:0,

    amount:0

}

]);






const [totals,setTotals] = useState({

    subtotal:0,

    gstAmount:0,

    grandTotal:0

});





const [loading,setLoading] = useState(false);






// ===============================
// CALCULATION
// ===============================


useEffect(()=>{


const updatedItems = items.map(item=>({

    ...item,

    amount:

    Number(item.quantity || 0)

    *

    Number(item.rate || 0)

}));





const subtotal = updatedItems.reduce(

    (sum,item)=>

    sum + item.amount,

    0

);





const extraCharges =

Number(formData.labourCost || 0)

+

Number(formData.installationCost || 0)

+

Number(formData.transportCost || 0)

+

Number(formData.otherCharges || 0);






let taxableAmount =

subtotal

+

extraCharges

-

Number(formData.discount || 0);





if(taxableAmount < 0){

    taxableAmount = 0;

}






const gstAmount =

(

taxableAmount

*

Number(formData.gstPercent || 0)

)

/100;






const grandTotal =

taxableAmount

+

gstAmount;







setTotals({

    subtotal,

    gstAmount,

    grandTotal

});





},[items,formData]);









// ===============================
// INPUT HANDLER
// ===============================


const handleInputChange=(e)=>{


setFormData({

    ...formData,

    [e.target.name]:e.target.value

});


};









// ===============================
// ITEM UPDATE
// ===============================


const handleItemChange=(index,field,value)=>{


const updatedItems = items.map((item,i)=>{


if(i===index){


return {


...item,


[field]:value


};


}


return item;


});



setItems(updatedItems);


};









// ===============================
// ADD ITEM
// ===============================


const addItemRow=()=>{


setItems([

...items,


{

materialName:"",

description:"",

quantity:1,

unit:"Nos",

rate:0,

amount:0

}


]);


};









// ===============================
// REMOVE ITEM
// ===============================


const removeItemRow=(index)=>{


if(items.length<=1)

return;




setItems(

items.filter(

(_,i)=>i!==index

)

);


};


// ===============================
// GENERATE PROFESSIONAL PDF
// ===============================


// SAVE QUOTATION API
// ===============================


const handleSaveAndDownload = async(e)=>{


e.preventDefault();





if(

!formData.customerName ||

!formData.mobileNumber

){


alert(

"Customer Name and Mobile Number Required"

);


return;


}





setLoading(true);





try{





const payload = {



customer_name:

formData.customerName,



company_name:

formData.companyName,



mobile_number:

formData.mobileNumber,



email:

formData.email || null,



address:

formData.address || null,



lead_source:

formData.leadSource,



work_type:

formData.workType,



material_type:

formData.materialType,



width_ft:0,



height_ft:0,



items:

items.map(item=>({


material_name:

item.materialName,


description:

item.description || "",


quantity:

Number(item.quantity || 0),


unit:

item.unit,


rate:

Number(item.rate || 0),


amount:

Number(item.quantity || 0)

*

Number(item.rate || 0)


})),



labour_cost:

Number(formData.labourCost || 0),



installation_cost:

Number(formData.installationCost || 0),



transport_cost:

Number(formData.transportCost || 0),



other_charges:

Number(formData.otherCharges || 0),



gst_percent:

Number(formData.gstPercent || 0),



discount:

Number(formData.discount || 0),



payment_terms:

formData.paymentTerms,



delivery_time:

formData.deliveryTime,



notes:

formData.notes || null


};







const response = await API.post(

"/quotation/create",

payload

);







const quotationId = response?.data?.data?.id;

if(quotationId){

    const pdfResponse = await API.get(
        `/quotation/pdf/${quotationId}`,
        {
            responseType:"blob"
        }
    );

    const fileURL = window.URL.createObjectURL(
        new Blob(
            [pdfResponse.data],
            {
                type:"application/pdf"
            }
        )
    );

    const link = document.createElement("a");

    link.href = fileURL;

    link.download =
    `${response?.data?.data?.quotation_no || "quotation"}.pdf`;

    document.body.appendChild(link);

    link.click();

    link.remove();

    window.URL.revokeObjectURL(fileURL);

}







alert(

`Quotation Created Successfully\nNo : ${
response?.data?.data?.quotation_no || "Generated"
}`

);





}

catch(error){



console.error(

"Quotation Error",

error

);




alert(

error?.response?.data?.detail ||

"Quotation Save Failed"

);



}

finally{


setLoading(false);


}


};


// ===============================
// RETURN UI
// ===============================


return (

<div className="quotation-container">



<h2 className="quotation-title">

Deepu Fabricator Quotation Panel

</h2>






<form onSubmit={handleSaveAndDownload}>





{/* QUOTATION NAME */}

<div className="form-group">


<label className="form-label">

Quotation Reference Name

</label>




<input

type="text"

value={quotationName}

onChange={(e)=>

setQuotationName(e.target.value)

}

className="input-field"

/>


</div>









{/* CUSTOMER DETAILS */}



<h3>

Customer Details

</h3>





<div className="grid-2-col">





<input

type="text"

name="customerName"

placeholder="Customer Name *"

value={formData.customerName}

onChange={handleInputChange}

className="input-field"

/>







<input

type="text"

name="mobileNumber"

placeholder="Mobile Number *"

value={formData.mobileNumber}

onChange={handleInputChange}

className="input-field"

/>








<input

type="email"

name="email"

placeholder="Email"

value={formData.email}

onChange={handleInputChange}

className="input-field"

/>







<input

type="text"

name="companyName"

placeholder="Company Name"

value={formData.companyName}

onChange={handleInputChange}

className="input-field"

/>





</div>








<textarea


name="address"


placeholder="Customer Address"


value={formData.address}


onChange={handleInputChange}


rows="3"


className="input-field"


/>









{/* WORK CONFIGURATION */}



<h3>

Work Configuration

</h3>







<div className="grid-2-col">



<select


name="workType"


value={formData.workType}


onChange={handleInputChange}


className="input-field"


>



<option>

Steel Gate / Grill

</option>



<option>

Rolling Shutter

</option>



<option>

Industrial Shed

</option>



<option>

Other Fabrication

</option>



</select>








<input

type="text"

name="materialType"

value={formData.materialType}

onChange={handleInputChange}

placeholder="Material Type"

className="input-field"

/>





</div>









{/* MATERIAL DETAILS */}



<h3>

Material Details

</h3>








<div className="table-scroll-wrapper">



<table className="material-table">



<thead>


<tr>


<th>

Material

</th>


<th>

Description

</th>


<th>

Qty

</th>


<th>

Unit

</th>


<th>

Rate

</th>


<th>

Amount

</th>


<th>

Action

</th>



</tr>


</thead>








<tbody>




{

items.map((item,index)=>(



<QuotationItem


key={index}


item={item}


index={index}


onItemChange={handleItemChange}


onRemoveRow={removeItemRow}


isDeleteDisabled={items.length <= 1}


/>



))


}






</tbody>







</table>



</div>









<button


type="button"


className="btn-add"


onClick={addItemRow}



>


➕ Add Material


</button>









{/* CHARGES */}



<h3>

Charges

</h3>








<div className="grid-3-col">






<input


type="number"


name="labourCost"


value={formData.labourCost}


onChange={handleInputChange}


placeholder="Labour Cost"


className="input-field"


/>







<input


type="number"


name="installationCost"


value={formData.installationCost}


onChange={handleInputChange}


placeholder="Installation Cost"


className="input-field"


/>







<input


type="number"


name="transportCost"


value={formData.transportCost}


onChange={handleInputChange}


placeholder="Transport Cost"


className="input-field"


/>






</div>








<div className="grid-2-col">






<input


type="number"


name="otherCharges"


value={formData.otherCharges}


onChange={handleInputChange}


placeholder="Other Charges"


className="input-field"


/>







<input


type="number"


name="gstPercent"


value={formData.gstPercent}


onChange={handleInputChange}


placeholder="GST Percentage"


className="input-field"


/>






</div>









<div className="grid-2-col">





<input


type="number"


name="discount"


value={formData.discount}


onChange={handleInputChange}


placeholder="Discount"


className="input-field"


/>








<input


type="text"


name="leadSource"


value={formData.leadSource}


onChange={handleInputChange}


placeholder="Lead Source"


className="input-field"


/>






</div>









{/* TERMS */}



<h3>

Terms & Conditions

</h3>








<div className="grid-2-col">





<input


type="text"


name="paymentTerms"


value={formData.paymentTerms}


onChange={handleInputChange}


placeholder="Payment Terms"


className="input-field"


/>








<input


type="text"


name="deliveryTime"


value={formData.deliveryTime}


onChange={handleInputChange}


placeholder="Delivery Time"


className="input-field"


/>






</div>









<textarea


name="notes"


placeholder="Additional Notes"


value={formData.notes}


onChange={handleInputChange}


rows="3"


className="input-field"


/>










{/* TOTAL SUMMARY */}



<div className="total-summary-panel">



<p>

Subtotal :

Rs. {totals.subtotal.toFixed(2)}

</p>






<p>

GST :

Rs. {totals.gstAmount.toFixed(2)}

</p>








<h2>

Grand Total :

Rs. {totals.grandTotal.toFixed(2)}

</h2>





</div>









<button


type="submit"


disabled={loading}


className="btn-submit"



>



{

loading

?

"Generating..."

:

"Generate Quotation"

}



</button>







</form>



</div>


);


// ===============================
// COMPONENT CLOSE
// ===============================


};





export default Quotation;



