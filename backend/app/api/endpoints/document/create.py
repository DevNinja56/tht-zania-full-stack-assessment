from django.http import JsonResponse  # type: ignore
from rest_framework.decorators import api_view  # type: ignore
from api.models import Document
import json
from drf_yasg import openapi  # type: ignore
from drf_yasg.utils import swagger_auto_schema  # type: ignore

# Define common request body schema for POST
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


# Create a new document
@swagger_auto_schema(
    method="post",
    request_body=document_schema,
    responses={201: "Document created", 400: "Invalid data"},
)
@api_view(["POST"])
def create_document(request):
    try:
        data = json.loads(request.body)
        document = Document.objects.create(
            type=data["type"], title=data["title"], position=data["position"]
        )
        return JsonResponse(
            {
                "id": document.id,
                "type": document.type,
                "title": document.title,
                "position": document.position,
            },
            status=201,
        )
    except KeyError:
        return JsonResponse({"error": "Missing required fields"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)