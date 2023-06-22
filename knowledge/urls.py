from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knowledge.views import (
    KnowledgeList,
    KnowledgeDetail,
    KnowledgeCreate,
)

urlpatterns = [
    path("", KnowledgeList.as_view(), name="knowledge-list"),
    path("<slug:slug>/", KnowledgeDetail.as_view(), name="knowledge-detail"),
    path(
        "<slug:slug>/create",
        KnowledgeCreate.as_view(),
        name="knowledge-create",
    ),
]
