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
    
    # non authenticated request
    response = client.json.post(url, json.dumps(data))
    assert response.status_code == 401

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


def test_retrieve_todo(client):
    user = f.create_user()
    todo = f.create_todo(user=user)

    url = reverse('todos-list')
    
    # non authenticated request
    response = client.json.get(url)
    assert response.status_code == 401

    client.login(user)

    response = client.json.get(url)
    assert response.status_code == 200
    assert response.data['count'] == 1
    expected_keys = [
        "id", "todo", "description", "is_completed", "created_at", "modified_at"
    ]
    assert set(response.data['results'][0].keys()) == set(expected_keys)
    assert response.data['results'][0]['id'] == str(todo.id)


def test_retrieve_one_todo(client):
    user = f.create_user()
    todo = f.create_todo(user=user)

    url = reverse('todos-detail', kwargs={'pk': todo.id})

    # non authenticated request
    response = client.json.get(url)
    assert response.status_code == 401

    client.login(user)

    response = client.json.get(url)
    assert response.status_code == 200
    expected_keys = [
        "id", "todo", "description", "is_completed", "created_at", "modified_at"
    ]
    assert set(response.data.keys()) == set(expected_keys)


def test_patch_todo(client):
    user = f.create_user()
    todo = f.create_todo(user=user, is_completed=False)

    url = reverse('todos-detail', kwargs={'pk': todo.id})
    data = {
        'is_completed': True
    }

    # non authenticated request
    response = client.json.patch(url, json.dumps(data))
    assert response.status_code == 401

    client.login(user)
    response = client.json.patch(url, json.dumps(data))
    assert response.status_code == 200
    expected_keys = [
        "id", "todo", "description", "is_completed", "created_at", "modified_at"
    ]
    assert set(response.data.keys()) == set(expected_keys)
    assert response.data['is_completed'] is True


def test_delete_todo(client):
    user = f.create_user()
    todo = f.create_todo(user=user, is_completed=False)

    url = reverse('todos-detail', kwargs={'pk': todo.id})

    # non authenticated request
    response = client.delete(url)
    assert response.status_code == 401

    client.login(user)
    response = client.delete(url)
    assert response.status_code == 204
