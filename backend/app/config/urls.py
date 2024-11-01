from django.urls import path, include  # type: ignore
from drf_yasg import openapi  # type: ignore
from rest_framework import permissions  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version="v1",
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/v1/", include("api.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]