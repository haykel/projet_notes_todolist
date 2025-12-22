from rest_framework.viewsets import ModelViewSet  # type: ignore[reportMissingImports]
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    """
    CRUD API for notes.

    - Create / update notes
    - Retrieve notes with their related todos
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
