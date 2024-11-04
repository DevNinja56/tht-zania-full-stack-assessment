from django.http import JsonResponse  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from api.models import Document
import json
from drf_yasg import openapi  # type: ignore
from drf_yasg.utils import swagger_auto_schema  # type: ignore

# Define common request body schema for PUT and PATCH
document_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "type": openapi.Schema(type=openapi.TYPE_STRING, description="Document type"),
        "title": openapi.Schema(type=openapi.TYPE_STRING, description="Document title"),
        "position": openapi.Schema(
            type=openapi.TYPE_INTEGER, description="Document position"
        ),
    },
)


# Update a document fully (PUT)
@swagger_auto_schema(
    method="put",
    request_body=document_schema,
    responses={200: "Document updated", 400: "Invalid data", 404: "Document not found"},
)
@api_view(["PUT"])
def update_document(request, id):
    """Update an existing document"""
    document = get_object_or_404(Document, pk=id)
    try:
        data = json.loads(request.body)
        if "type" in data:
            document.type = data["type"]
        if "title" in data:
            document.title = data["title"]
        if "position" in data:
            document.position = data["position"]
        document.save()
        return JsonResponse(
            {
                "id": document.id,
                "type": document.type,
                "title": document.title,
                "position": document.position,
            }
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Partially update a document (PATCH)
@swagger_auto_schema(
    method="patch",
    request_body=document_schema,
    responses={
        200: "Document partially updated",
        400: "Invalid data",
        404: "Document not found",
    },
)
@api_view(["PATCH"])
def partial_update_document(request, id):
    document = get_object_or_404(Document, pk=id)
    try:
        data = json.loads(request.body)
        if "type" in data:
            document.type = data["type"]
        if "title" in data:
            document.title = data["title"]
        if "position" in data:
            document.position = data["position"]
        document.save()
        return JsonResponse(
            {
                "id": document.id,
                "type": document.type,
                "title": document.title,
                "position": document.position,
            }
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "documents": openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=document_schema,
                description="List of documents to update",
            )
        },
    ),
    responses={
        200: "Documents updated",
        400: "Invalid data",
        404: "Document not found",
    },
)
@api_view(["POST"])
def batch_update_documents(request):
    """Batch update the positions of multiple documents"""
    try:
        data = json.loads(request.body)
        documents_data = data.get("documents", [])

        if not isinstance(documents_data, list):
            return JsonResponse(
                {"error": "Invalid data format, expected a list of documents."},
                status=400,
            )

        for doc_data in documents_data:
            doc_id = doc_data.get("id")
            new_position = doc_data.get("position")

            # Validate each document's data
            if doc_id is None or new_position is None:
                return JsonResponse(
                    {"error": "Each document must have an 'id' and 'position'."},
                    status=400,
                )

            # Retrieve and update the document
            document = get_object_or_404(Document, pk=doc_id)
            document.position = new_position
            document.save()

        return JsonResponse({"message": "Documents updated successfully"}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
