import pytest
from notes.models import Note

@pytest.mark.django_db
def test_create_note():
    """
    A note should persist title and content.
    """
    note = Note.objects.create(
        title="Meeting notes",
        content="Important points"
    )

    assert note.title == "Meeting notes"
    assert note.content == "Important points"
