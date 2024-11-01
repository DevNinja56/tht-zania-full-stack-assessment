import React, { useEffect, useState } from "react";
import { fetchDocuments } from "../api/apiClient";
import { Document } from "../types/DocumentType";
import Grid from "../components/Grid";
import Overlay from "../components/Overlay";
import Spinner from "../components/Spinner";

const HomePage: React.FC = () => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    (async () => {
      setLoading(true);
      const fetchedDocuments = await fetchDocuments();
      setDocuments(fetchedDocuments);
      setLoading(false);
    })();
  }, []);

  const reorderCards = (fromIndex: number, toIndex: number) => {
    const updatedDocs = [...documents];
    const [movedDoc] = updatedDocs.splice(fromIndex, 1);
    updatedDocs.splice(toIndex, 0, movedDoc);
    setDocuments(updatedDocs);
  };

  return (
    <div>
      <h1>Document Viewer</h1>
      {loading ? (
        <Spinner />
      ) : (
        <Grid
          documents={documents}
          onReorder={reorderCards}
          onCardClick={(index) => {
            setSelectedImage(`/images/${documents[index].type}.webp`);
          }}
        />
      )}
      {selectedImage && (
        <Overlay
          imageUrl={selectedImage}
          onClose={() => setSelectedImage(null)}
        />
      )}
    </div>
  );
};

export default HomePage;
