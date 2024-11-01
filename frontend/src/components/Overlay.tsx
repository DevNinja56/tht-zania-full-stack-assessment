import React from "react";
import "../styles/Overlay.css";

interface OverlayProps {
  imageUrl: string;
  onClose: () => void;
}

const Overlay: React.FC<OverlayProps> = ({ imageUrl, onClose }) => {
  // Close overlay on pressing the Escape key
  React.useEffect(() => {
    const handleEsc = (event: KeyboardEvent) => {
      if (event.key === "Escape") onClose();
    };
    window.addEventListener("keydown", handleEsc);
    return () => window.removeEventListener("keydown", handleEsc);
  }, [onClose]);

  return (
    <div className="overlay-backdrop" onClick={onClose}>
      <div className="overlay-content" onClick={(e) => e.stopPropagation()}>
        <img className="overlay-image" src={imageUrl} alt="Document" />
      </div>
    </div>
  );
};

export default Overlay;
