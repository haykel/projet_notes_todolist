import pytest
from notes.models import Note


@pytest.mark.django_db
def test_note_model_persists_title_and_content():
    """
    Note model should persist title and content correctly.
    """
    note = Note.objects.create(
        title="Meeting notes",
        content="Important points"
    )

    assert note.title == "Meeting notes"
    assert note.content == "Important points"
