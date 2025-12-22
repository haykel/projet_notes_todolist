import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from notes.models import Note
from todos.models import Todo


@pytest.mark.django_db
class TestTodoAPI:
    """
    API tests for Todo endpoints.
    Covers CRUD operations, visibility rules,
    and JWT authentication requirements.
    """

    def setup_method(self):
        """
        Create an authenticated user and a note for all tests.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.force_authenticate(user=self.user)

        self.note = Note.objects.create(title="Test note")

    def test_todos_requires_authentication(self):
        """
        Todos API must be protected by authentication.
        """
        client = APIClient()
        response = client.get("/api/todos/")
        assert response.status_code == 401

    def test_create_todo_with_note(self):
        """
        A todo linked to a note can be created via the API.
        """
        response = self.client.post(
            "/api/todos/",
            {
                "title": "API Todo",
                "status": "todo",
                "note_id": self.note.id,
            },
            format="json",
        )

        assert response.status_code == 201
        assert response.data["title"] == "API Todo"
        assert response.data["note_id"] == self.note.id

    def test_list_todos_only_returns_linked_todos(self):
        """
        Only todos linked to a note are visible in the API.
        """
        Todo.objects.create(title="Hidden todo")  # no note
        Todo.objects.create(title="Visible todo", note=self.note)

        response = self.client.get("/api/todos/")

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["title"] == "Visible todo"

    def test_retrieve_todo(self):
        """
        A linked todo can be retrieved by id.
        """
        todo = Todo.objects.create(
            title="Retrieve me",
            note=self.note,
        )

        response = self.client.get(f"/api/todos/{todo.id}/")

        assert response.status_code == 200
        assert response.data["title"] == "Retrieve me"

    def test_update_todo(self):
        """
        A todo can be updated via the API.
        """
        todo = Todo.objects.create(
            title="Old title",
            note=self.note,
        )

        response = self.client.patch(
            f"/api/todos/{todo.id}/",
            {"status": "done"},
            format="json",
        )

        assert response.status_code == 200
        assert response.data["status"] == "done"

    def test_delete_todo(self):
        """
        A todo can be deleted via the API.
        """
        todo = Todo.objects.create(
            title="To delete",
            note=self.note,
        )

        response = self.client.delete(f"/api/todos/{todo.id}/")

        assert response.status_code == 204
        assert Todo.objects.count() == 0

    def test_orphan_todo_is_not_accessible(self):
        """
        A todo without a note should not be accessible via the API.
        """
        todo = Todo.objects.create(title="Orphan")

        response = self.client.get(f"/api/todos/{todo.id}/")

        assert response.status_code == 404
