import pytest
from rest_framework.test import APIClient

from students.models import Students

client = APIClient()


@pytest.mark.django_db
def test_create_student():
    payload = {
        "pk": 3,
        "name": "example",
        "email": "example@example.com",
        "document": "report",
        "phone": "67686986",
    }
    res = client.post("/api/students/", payload)
    assert res.status_code == 201


@pytest.mark.django_db
def test_get_students():
    response = client.get("/api/students/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_student():
    payload = {
        "pk": 1,
        "name": "example",
        "email": "example@example.com",
        "document": "report",
        "phone": "67686986",
    }
    errorPayload = {
        "pk": 7,
        "name": "example",
        "email": "example@example.com",
        "document": "report",
        "phone": "67686986",
    }
    errorRes = client.put(f"/api/students/{errorPayload['pk']}", errorPayload)
    res = client.put(f"/api/students/{payload['pk']}", payload)
    assert errorRes.status_code == 404
    assert res.status_code == 204


@pytest.mark.django_db
def test_delete_students():
    payload = {
        "pk": 3,
        "name": "example",
        "email": "example@example.com",
        "document": "report",
        "phone": "67686986",
    }
    client.post("/api/students/", payload)
    resDelete = client.delete("/api/students/3")
    resErrorDelete = client.delete("/api/students/78")
    assert resDelete.status_code == 204
    assert resErrorDelete.status_code == 404


@pytest.mark.django_db
def test_student_count():
    assert Students.objects.count() == 1
