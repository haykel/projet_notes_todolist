import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from notes.models import Note
from todos.models import Todo


@pytest.mark.django_db
class TestNoteAPI:
    """
    API tests for Note endpoints.
    Covers CRUD operations, relations with todos,
    and JWT authentication requirements.
    """

    def setup_method(self):
        """
        Create an authenticated user for all tests.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="admin",
            password="admin"
        )
        self.client.force_authenticate(user=self.user)

    def test_notes_requires_authentication(self):
        """
        Notes API must be protected by authentication.
        """
        client = APIClient()
        response = client.get("/api/notes/")
        assert response.status_code == 401

    def test_create_note(self):
        """
        A note can be created via the API.
        """
        response = self.client.post(
            "/api/notes/",
            {
                "title": "Test note",
                "content": "Some content",
            },
            format="json",
        )

        assert response.status_code == 201
        assert response.data["title"] == "Test note"
        assert response.data["content"] == "Some content"

    def test_list_notes(self):
        """
        Notes can be listed via the API.
        """
        Note.objects.create(title="Note 1")
        Note.objects.create(title="Note 2")

        response = self.client.get("/api/notes/")

        assert response.status_code == 200
        assert len(response.data) == 2

    def test_retrieve_note_with_todos(self):
        """
        Retrieving a note returns its related todos.
        """
        note = Note.objects.create(title="Parent note")

        Todo.objects.create(title="Todo 1", note=note)
        Todo.objects.create(title="Todo 2", note=note)

        response = self.client.get(f"/api/notes/{note.id}/")

        assert response.status_code == 200
        assert response.data["title"] == "Parent note"
        assert "todos" in response.data
        assert len(response.data["todos"]) == 2

    def test_update_note(self):
        """
        A note can be updated via the API.
        """
        note = Note.objects.create(title="Old title")

        response = self.client.patch(
            f"/api/notes/{note.id}/",
            {"title": "New title"},
            format="json",
        )

        assert response.status_code == 200
        assert response.data["title"] == "New title"

    def test_delete_note(self):
        """
        A note can be deleted via the API.
        """
        note = Note.objects.create(title="To be deleted")

        response = self.client.delete(f"/api/notes/{note.id}/")

        assert response.status_code == 204
        assert Note.objects.count() == 0
