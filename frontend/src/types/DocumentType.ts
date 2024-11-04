export interface Document {
  id: number;
  type: string;
  title: string;
  position: number;
}

export interface PaginatedDocument {
  count: number;
  next: string | null;
  previous: string | null;
  results: Document[];
}