from rest_framework import serializers
from .models import Note
from todos.models import Todo


class NoteTodoSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for todos linked to a note.
    Used only for read operations to avoid circular writes.
    """

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "status",
        ]


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Note.
    Includes related todos in read-only mode.
    """

    # Reverse relation via related_name="todos" on Todo.note
    todos = NoteTodoSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "content",
            "todos",
            "created_at",
            "updated_at",
        ]
