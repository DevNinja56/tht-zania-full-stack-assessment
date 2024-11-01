from django.http import JsonResponse  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from api.models import Document
from drf_yasg.utils import swagger_auto_schema  # type: ignore
import json

# Delete a document
@swagger_auto_schema(
    method="delete", responses={204: "Document deleted", 404: "Document not found"}
)
@api_view(["DELETE"])
def delete_document(request, id):
    """Delete a specific document by ID"""
    try:
        document = get_object_or_404(Document, pk=id)
        document.delete()
        return JsonResponse({}, status=204)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
