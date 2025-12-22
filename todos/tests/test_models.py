import pytest
from todos.models import Todo

@pytest.mark.django_db
def test_todo_default_status():
    """
    A todo defaults to 'todo' status.
    """
    todo = Todo.objects.create(title="Buy milk")
    assert todo.status == "todo"
