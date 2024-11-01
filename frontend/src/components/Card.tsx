import React, { useState } from "react";
import { Document } from "../types/DocumentType";
import Spinner from "./Spinner";

interface CardProps {
  document: Document;
  onClick?: () => void;
}

const Card: React.FC<CardProps> = ({ document, onClick }) => {
  const [loading, setLoading] = useState(true);

  return (
    <div className="card" onClick={onClick}>
      {loading && <Spinner />}
      <img
        src={`/images/${document.type}.webp`}
        alt={document.title}
        onLoad={() => setLoading(false)}
        style={{ display: loading ? "none" : "block", height: 200, width: 200 }}
      />
      <h3>{document.title}</h3>
    </div>
  );
};

export default Card;
