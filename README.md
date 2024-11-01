# Project Overview

This project implements a full-stack application for managing and displaying document data using React, Python (Django REST Framework), and SQLite. It is structured in five parts, each building upon the last to create a complete application that allows for CRUD operations on document data. The front end displays a grid of documents as interactive cards, each containing a document type, title, and position. Users can reorder cards via drag-and-drop and view images in an overlay.

### Key Features: 
#### Frontend (React):

- Loads and displays a static JSON file of document data as a grid of cards.
- Allows reordering of cards through drag-and-drop.
- Shows images in an overlay, with ESC to close.
- Automatically saves data to the backend every five seconds if changes have been made, showing a loading spinner and elapsed time since the last save.

#### Backend (Django, SQLite):

- Stores document data in a SQLite table.
- Provides REST API endpoints to retrieve, add, update, and delete document records.
- Implements a Dockerized environment with Docker Compose for easy deployment and scalability.

#### Documentation and API Design:

- Swagger UI for interactive API documentation.
- Thoughtful API design for long-term maintenance, including error handling, versioning, and extensibility.

## Setup Docker

Ensure you have Docker and Docker Compose installed on your system.

- [Get Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

### Usage

To start the Docker containers, run

```bash
docker-compose up -d
```

To stop the Docker container, run:

```bash
docker-compose down
```
