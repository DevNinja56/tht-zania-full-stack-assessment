import React from "react";
import { BounceLoader } from "react-spinners";
import "../styles/Spinner.css";

interface SpinnerProps {
  message?: string;
}

const Spinner: React.FC<SpinnerProps> = ({ message }) => (
  <div className="spinner-overlay">
    <BounceLoader color="#36D7B7" />
    <p>{message || "Loading"}...</p>
  </div>
);

export default Spinner;
