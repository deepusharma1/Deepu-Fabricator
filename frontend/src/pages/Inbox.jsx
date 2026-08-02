import React from "react";
import LiveInbox from "../components/InboxPage/LiveInbox";

const Inbox = () => {
  return (
    <div className="inbox-page-wrapper" style={{ padding: "20px", minHeight: "80vh" }}>
      <LiveInbox />
    </div>
  );
};

export default Inbox;


