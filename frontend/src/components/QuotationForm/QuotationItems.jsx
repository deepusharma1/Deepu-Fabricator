import React from "react";

const QuotationItem = ({
  item,
  index,
  onItemChange,
  onRemoveRow,
  isDeleteDisabled
}) => {

  return (

    <tr className="quotation-item-row">

      <td>
        <input
          type="text"
          value={item.materialName}
          placeholder="Steel Pipe, Channel"
          onChange={(e)=>
            onItemChange(index,"materialName",e.target.value)
          }
          className="table-input"
          required
        />
      </td>


      <td>
        <input
          type="text"
          value={item.description}
          placeholder="Dimensions / Grade"
          onChange={(e)=>
            onItemChange(index,"description",e.target.value)
          }
          className="table-input"
        />
      </td>


      <td>

        <input
          type="number"
          value={item.quantity}
          min="1"
          onChange={(e)=>
            onItemChange(index,"quantity",e.target.value)
          }
          className="table-input"
          required
        />

      </td>



      <td>

        <input
          type="number"
          value={item.rate}
          min="0"
          placeholder="0.00"
          onChange={(e)=>
            onItemChange(index,"rate",e.target.value)
          }
          className="table-input"
          required
        />

      </td>



      <td className="item-total">

        Rs. {
          (
            Number(item.quantity || 0) *
            Number(item.rate || 0)
          ).toFixed(2)
        }

      </td>



      <td className="item-action">

        {
          !isDeleteDisabled &&

          <button
            type="button"
            onClick={() => onRemoveRow(index)}
            className="btn-delete"
          >
            Delete
          </button>

        }

      </td>


    </tr>

  );
};


export default QuotationItem;

