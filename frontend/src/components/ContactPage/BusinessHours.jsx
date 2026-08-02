import React from "react";
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableRow, Paper } from "@mui/material";
import "./BusinessHours.css";

function BusinessHours() {
  const hoursData = [
    { day: "Monday", time: "9:00 AM - 7:00 PM" },
    { day: "Tuesday", time: "9:00 AM - 7:00 PM" },
    { day: "Wednesday", time: "9:00 AM - 7:00 PM" },
    { day: "Thursday", time: "9:00 AM - 7:00 PM" },
    { day: "Friday", time: "9:00 AM - 7:00 PM" },
    { day: "Saturday", time: "9:00 AM - 7:00 PM" },
    { day: "Sunday", time: "Closed", isClosed: true },
  ];

  return (
    <Box className="hours-section">
      <Typography variant="h5" className="hours-title">
        Our Business Hours
      </Typography>
      <Typography variant="body2" className="hours-subtitle">
        Plan your visit or call us during our functional timings
      </Typography>

      <TableContainer component={Paper} className="hours-table-container">
        <Table>
          <TableBody>
            {hoursData.map((row) => (
              <TableRow key={row.day} className="hours-row">
                <TableCell component="th" scope="row" className="day-cell">
                  {row.day}
                </TableCell>
                <TableCell 
                  align="right" 
                  className={`time-cell ${row.isClosed ? "closed-status" : ""}`}
                >
                  {row.time}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default BusinessHours;


