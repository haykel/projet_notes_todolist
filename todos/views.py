from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(ModelViewSet):
    """
    CRUD API for todos.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
