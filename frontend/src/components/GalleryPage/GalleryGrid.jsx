import "./GalleryGrid.css";

import gate1 from "../../assets/gallery/gate1.jpg";
import gate2 from "../../assets/gallery/gate2.jpg";
import shutter1 from "../../assets/gallery/shutter1.jpg";
import shed1 from "../../assets/gallery/shed1.jpg";
import shed2 from "../../assets/gallery/shed2.jpg";
import lift1 from "../../assets/gallery/lift1.jpg";
import railing1 from "../../assets/gallery/railing1.jpg";
import staircase1 from "../../assets/gallery/staircase1.jpg";

const projects = [
  { title:"Steel Gate", category:"Gate", image:gate1 },
  { title:"Designer Steel Gate", category:"Gate", image:gate2 },
  { title:"Rolling Shutter", category:"Shutter", image:shutter1 },
  { title:"Industrial Shed", category:"Shed", image:shed1 },
  { title:"Warehouse Shed", category:"Shed", image:shed2 },
  { title:"Hydraulic Scissor Lift", category:"Lift", image:lift1 },
  { title:"MS Railing", category:"Railing", image:railing1 },
  { title:"Steel Staircase", category:"Staircase", image:staircase1 }
];


function GalleryGrid(){

return(

<section className="gallery-section">

<div className="container">


<div className="gallery-title">

<span>OUR GALLERY</span>

<h2>
Our Latest Fabrication Projects
</h2>

<p>
We manufacture high-quality steel gates, rolling shutters,
hydraulic scissor lifts, industrial sheds, railings and
custom fabrication work.
</p>

</div>



<div className="gallery-grid">

{
projects.map((item,index)=>(

<div className="gallery-card" key={index}>

<img 
src={item.image}
alt={item.title}
/>


<div className="gallery-overlay">

<h3>
{item.title}
</h3>

<span>
{item.category}
</span>

</div>


</div>

))
}


</div>


</div>

</section>

)

}


export default GalleryGrid;

