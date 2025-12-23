from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    """
    CRUD API for todos.

    For now, todos without a related note are hidden
    from list and detail endpoints.
    """

    serializer_class = TodoSerializer


    def get_queryset(self):
        """
        Hide todos that are not linked to any note.
        This is a temporary business rule.
        """
        return Todo.objects.filter(note__isnull=False)
