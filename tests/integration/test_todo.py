# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_authenticated_user_can_create_todo(client):
    user = f.create_user()

    data = {
        "todo": "blah blah"
    }
    url = reverse('todos-list')
    client.login(user)
    response = client.json.post(url, json.dumps(data))
    assert response.status_code == 201
    expected_keys = [
        "id", "todo", "description", "is_completed", "created_at", "modified_at"
    ]
    assert set(response.data.keys()) == set(expected_keys)

    user.refresh_from_db()
    assert user.todos.exists() is True
    assert user.todos.count() == 1


def test_non_authenticated_user_cannot_create_todo(client):
    data = {
        "todo": "blah blah"
    }
    url = reverse('todos-list')
    response = client.json.post(url, json.dumps(data))
    assert response.status_code == 401
