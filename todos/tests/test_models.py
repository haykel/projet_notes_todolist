import pytest
from notes.models import Note
from todos.models import Todo

@pytest.mark.django_db
def test_todo_default_status():
    """
    A todo defaults to 'todo' status.
    """
    todo = Todo.objects.create(title="Buy milk")
    assert todo.status == "todo"

@pytest.mark.django_db
def test_todo_can_link_note():
    note = Note.objects.create(title="Daily note")
    todo = Todo.objects.create(title="Read", note=note)

    assert todo.note == note
    