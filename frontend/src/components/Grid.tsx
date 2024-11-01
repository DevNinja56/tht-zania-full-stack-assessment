import React from "react";
import Card from "./Card";
import { Document } from "../types/DocumentType";
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
  DragEndEvent,
} from "@dnd-kit/core";
import {
  arrayMove,
  SortableContext,
  sortableKeyboardCoordinates,
  rectSortingStrategy,
} from "@dnd-kit/sortable";
import { SortableItem } from "./SortableItem";
import "../styles/Grid.css";

interface GridProps {
  documents: Document[];
  onReorder: (fromIndex: number, toIndex: number) => void;
  onCardClick: (index: number) => void;
}

const Grid: React.FC<GridProps> = ({ documents, onReorder, onCardClick }) => {
  const sensors = useSensors(
    useSensor(PointerSensor),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    })
  );

  const handleDragEnd = (event: DragEndEvent) => {
    const { active, over } = event;

    if (over && active.id !== over.id) {
      const oldIndex = documents.findIndex(
        (item, index) => `${item.type}-${index}` === active.id
      );
      const newIndex = documents.findIndex(
        (item, index) => `${item.type}-${index}` === over.id
      );
      onReorder(oldIndex, newIndex);
    }
  };

  return (
    <DndContext
      sensors={sensors}
      collisionDetection={closestCenter}
      onDragEnd={handleDragEnd}
    >
      <SortableContext
        items={documents.map((doc, index) => `${doc.type}-${index}`)}
        strategy={rectSortingStrategy}
      >
        <div className="grid">
          {documents.map((document, index) => (
            <SortableItem
              key={`${document.type}-${index}`}
              id={`${document.type}-${index}`}
              onClick={() => {
                onCardClick(index);
              }}
            >
              <Card document={document} />
            </SortableItem>
          ))}
        </div>
      </SortableContext>
    </DndContext>
  );
};

export default Grid;
