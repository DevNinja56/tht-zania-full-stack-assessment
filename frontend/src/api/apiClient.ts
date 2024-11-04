import axios from "axios";
import { Document, PaginatedDocument } from "../types/DocumentType";

const API_BASE_URL =
  process.env.REACT_APP_BACKEND_URL || "http://localhost:8000/api/v1";

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: { "Content-Type": "application/json" },
});

export const fetchDocuments = async (): Promise<Document[]> => {
  try {
    const response = await apiClient.get<PaginatedDocument>("/documents");
    return response.status === 200 ? response.data.results : [];
  } catch (error) {
    console.error("Error fetching documents:", error);
    return [];
  }
};

export const batchUpdateDocuments = async (documents: Document[]) => {
  try {
    const response = await apiClient.post<Document[]>(
      `documents/batch-update`,
      {
        documents,
      }
    );
    return response.status === 200 ? response.data : null;
  } catch (error) {
    console.error("Failed to save order:", error);
  }
};
