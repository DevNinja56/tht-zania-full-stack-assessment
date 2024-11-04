import React, { useEffect, useState, useRef } from "react";
import { fetchDocuments, batchUpdateDocuments } from "../api/apiClient";
import { Document } from "../types/DocumentType";
import Grid from "../components/Grid";
import Overlay from "../components/Overlay";
import Spinner from "../components/Spinner";
import { formatTimeAgo } from "../utils/helperFunctions";

const HomePage: React.FC = () => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [timeSinceLastSave, setTimeSinceLastSave] = useState(0);
  const [hasChanges, setHasChanges] = useState(false);

  const saveIntervalRef = useRef<NodeJS.Timeout | null>(null);

  // Load documents on mount
  useEffect(() => {
    const loadDocuments = async () => {
      setLoading(true);
      try {
        const fetchedDocuments = await fetchDocuments();
        setDocuments(fetchedDocuments.sort((a, b) => a.position - b.position));
      } catch (error) {
        console.error("Failed to fetch documents:", error);
      } finally {
        setTimeout(() => setLoading(false), 1000);
      }
    };
    loadDocuments();
  }, []);

  // eslint-disable-next-line react-hooks/exhaustive-deps
  const saveDocuments = async () => {
    setIsSaving(true);
    try {
      await batchUpdateDocuments(documents);
      setHasChanges(false); // Reset change flag
      setTimeSinceLastSave(0); // Reset save timer
    } catch (error) {
      console.error("Failed to save documents:", error);
    } finally {
      setTimeout(() => setIsSaving(false), 1000);
    }
  };

  // Save changes every 5 seconds if there are changes
  useEffect(() => {
    saveIntervalRef.current = setInterval(() => {
      if (hasChanges) {
        saveDocuments();
      }
    }, 5000);

    return () => clearInterval(saveIntervalRef.current!);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [hasChanges]);

  // Increment time since last save
  useEffect(() => {
    const timer = setInterval(() => {
      setTimeSinceLastSave((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const reorderCards = (fromIndex: number, toIndex: number) => {
    const updatedDocs = [...documents];
    const [movedDoc] = updatedDocs.splice(fromIndex, 1);
    updatedDocs.splice(toIndex, 0, movedDoc);

    // Update positions based on new order
    const reorderedDocs = updatedDocs.map((doc, index) => ({
      ...doc,
      position: index,
    }));

    setDocuments(reorderedDocs);
    setHasChanges(true);
  };

  return (
    <div>
      <h1>Document Viewer</h1>
      {loading ? (
        <Spinner />
      ) : documents.length > 0 ? (
        <Grid
          documents={documents}
          onReorder={reorderCards}
          onCardClick={(index) => {
            setSelectedImage(`/images/${documents[index].type}.webp`);
          }}
        />
      ) : (
        <p>No documents found.</p>
      )}
      {isSaving && <Spinner message="Saving" />}
      <p>Time since last save: {formatTimeAgo(timeSinceLastSave)}</p>
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
