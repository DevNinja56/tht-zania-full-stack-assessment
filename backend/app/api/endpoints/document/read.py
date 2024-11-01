from django.http import JsonResponse  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from api.models import Document
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from drf_yasg import openapi  # type: ignore
from django.core.paginator import Paginator  # type: ignore
import json


# List all documents with pagination and filtering
@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "type",
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Filter by document type",
        ),
        openapi.Parameter(
            "title",
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="Filter by document title",
        ),
        openapi.Parameter(
            "position",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description="Filter by document position",
        ),
        openapi.Parameter(
            "page",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description="Page number for pagination",
        ),
        openapi.Parameter(
            "page_size",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description="Number of items per page",
        ),
    ],
    responses={200: "List of documents"},
)
@api_view(["GET"])
def list_documents(request):
    try:
        documents = Document.objects.all()

        # Filtering
        doc_type = request.GET.get("type")
        title = request.GET.get("title")
        position = request.GET.get("position")

        if doc_type:
            documents = documents.filter(type__icontains=doc_type)
        if title:
            documents = documents.filter(title__icontains=title)
        if position:
            documents = documents.filter(position=position)

        # Pagination
        page_number = request.GET.get("page", 1)
        page_size = request.GET.get("page_size", 10)
        paginator = Paginator(documents, page_size)
        page_obj = paginator.get_page(page_number)

        results = list(page_obj.object_list.values())

        return JsonResponse(
            {
                "count": paginator.count,
                "next": page_obj.next_page_number() if page_obj.has_next() else None,
                "previous": (
                    page_obj.previous_page_number() if page_obj.has_previous() else None
                ),
                "results": results,
            }
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Retrieve a single document by ID
@swagger_auto_schema(
    method="get", responses={200: "Document details", 404: "Document not found"}
)
@api_view(["GET"])
def retrieve_document(request, id):
    try:
        document = get_object_or_404(Document, pk=id)
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
