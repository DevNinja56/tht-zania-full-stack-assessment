import axios from "axios";
import { Document } from "../types/DocumentType";
import { initialDocuments } from "../utils/documentData";

const API_BASE_URL =
  process.env.REACT_APP_BACKEND_URL || "http://localhost:8000/api";

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: { "Content-Type": "application/json" },
});

export const fetchDocuments = async (): Promise<Document[]> => {
  try {
    const response = await apiClient.get<Document[]>("/documents");
    return response.data.length ? response.data : initialDocuments;
  } catch (error) {
    console.error("Error fetching documents:", error);
    return initialDocuments;
  }
};
