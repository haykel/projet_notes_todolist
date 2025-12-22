import pytest 
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_todo_api():
    client = APIClient()

    response = client.post(
        "/api/todos/",
        {"title": "API Todo"},
        format="json"
    )

    assert response.status_code == 201
    assert response.data["title"] == "API Todo"

