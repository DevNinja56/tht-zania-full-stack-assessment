from django.urls import path # type: ignore
from api.endpoints import (
    document
)

# Paths ----------------------------------------------------------------------------------------------------------------
urlpatterns = [
    # Document
    path('documents', document.read.list_documents, name='list-documents'),
    path('documents/create', document.create.create_document, name='create-document'),
    path('documents/<int:id>', document.read.retrieve_document, name='retrieve-document'),
    path('documents/batch-update', document.update.batch_update_documents, name='batch-update-documents'),
    path('documents/<int:id>/update', document.update.update_document, name='update-document'),
    path('documents/<int:id>/partial-update', document.update.partial_update_document, name='partial-update-document'),
    path('documents/<int:id>/delete', document.delete.delete_document, name='delete-document'),
]
