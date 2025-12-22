import pytest
from notes.models import Note
from todos.models import Todo


@pytest.mark.django_db
def test_todo_model_has_default_status():
    """
    Todo model should default to 'todo' status.
    """
    todo = Todo.objects.create(title="Buy milk")
    assert todo.status == "todo"


@pytest.mark.django_db
def test_todo_model_can_be_linked_to_note():
    """
    Todo model can be linked to a note.
    """
    note = Note.objects.create(title="Daily note")
    todo = Todo.objects.create(title="Read", note=note)

    assert todo.note == note
