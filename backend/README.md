# Project Documentation

This project provides a simple **THT Django REST API** for managing documents. The API allows users to create, retrieve, update, and delete **(CRUD)** documents. Each document has a type, title, and position attribute, which can be used to organize and identify documents in the database.

## Project Setup

1. **Install Dependencies:** Ensure you have pip installed, then install the required Python dependencies.

   ```bash
   pip3 install -r requirements.txt
   ```

2. **Database Setup:**
   This project is configured to use **PostgreSQL**. Ensure you have PostgreSQL running, or update the database settings in settings.py to use a different database (e.g., SQLite for local development).

3. **Run Migrations:** Apply database migrations to create the necessary tables.

   ```bash
   python3 manage.py migrate
   ```

4. **Seed Initial Data (Optional):** To seed some initial document data into the database, run:

   ```bash
   python3 manage.py seed
   ```

5. **Run the Server:** Start the Django development server.

   ```bash
   python3 manage.py runserver
   ```

## Access Swagger Documentation:

Swagger documentation is available at [Documentation](http://localhost:8000/swagger/), where you can view and test the API endpoints.
3:17

## Interactive API Documentation

To make API usage easier, Swagger UI is integrated for interactive documentation. You can access it at:

- [Swagger UI](http://localhost:8000/swagger/)
- [ReDoc](http://localhost:8000/redoc/)

In Swagger, you can view the request body, try out API requests, and see the response structure for each endpoint.

## Architecture and API Design Approach

**Simple, Flat Structure:** The project structure is kept simple, with one Document model representing the core entity. The flat structure is suitable for this small API without complex relationships or nested data.

1. **Function-Based Views:**

   - We used function-based views to keep the code straightforward and understandable. Each **CRUD** operation has its own function (e.g., create_document, get_all_documents), providing a clear separation of functionality.

   - The request body schema is documented manually using **openapi.Schema** since we didn't use DRF serializers. This approach provides flexibility, as the request body structure is defined directly in the view using @swagger_auto_schema.

2. **Database:**

   - SQLite was chosen as it's lightweight and ideal for development and testing.

   - The database configuration is minimal, and migrations are used to create tables automatically based on the model definition.

3. **Swagger Documentation:**

   - The swagger library is integrated to automatically generate API documentation. Each endpoint has a clearly defined request body, making it easier for developers to understand what data is expected.

   - The manual schema definition for the request body was used to ensure that all required and optional fields are explicitly shown in the documentation.

4. **Error Handling:**

   - Basic error handling is in place, with appropriate HTTP status codes returned for common errors (e.g., 400 Bad Request, 404 Not Found).

   - The JsonResponse class is used for consistent JSON responses across all endpoints.
