from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from todos.views import TodoViewSet
from notes.views import NoteViewSet

router = DefaultRouter()
router.register(r"todos", TodoViewSet, basename="todo")
router.register(r"notes", NoteViewSet, basename="note")


urlpatterns = [
    path("admin/", admin.site.urls),

    # API
    path("api/", include(router.urls)),

    # OpenAPI / Swagger
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
