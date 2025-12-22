from rest_framework import serializers
from .models import Todo
from notes.models import Note


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model.
    """

    note_id = serializers.PrimaryKeyRelatedField(
        source="note",
        queryset=Note.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "status",
            "note_id",
            "created_at",
        ]
