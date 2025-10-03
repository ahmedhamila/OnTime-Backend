from django.contrib.auth import get_user_model

import pytest

from rest_framework.test import APIClient

from src.users.models.Admin import Admin
from src.users.models.ChefChantier import ChefChantier


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user():
    return get_user_model().objects.create_user(
        email="admin@example.com",
        username="admin@example.com",
        password="password123",
        user_type="Admin",
        phone_number="+1234567890",
    )


@pytest.fixture
def chef_chantier_user():
    return get_user_model().objects.create_user(
        email="chef@example.com",
        username="chef@example.com",
        password="password123",
        user_type="ChefChantier",
        phone_number="+1234567891",
    )


@pytest.fixture
def admin_instance(admin_user):
    return Admin.objects.create(user=admin_user)


@pytest.fixture
def chef_chantier_instance(chef_chantier_user):
    return ChefChantier.objects.create(user=chef_chantier_user)


@pytest.mark.django_db
def test_admin_create(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = "http://127.0.0.1:8000/api/users/admins/"
    data = {"user": admin_user.id, "is_super_user": True}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert Admin.objects.count() == 1
    assert Admin.objects.first().user == admin_user


@pytest.mark.django_db
def test_admin_permissions(api_client, admin_user, chef_chantier_user):
    api_client.force_authenticate(user=admin_user)
    url = "http://127.0.0.1:8000/api/users/admins/"
    data = {"user": chef_chantier_user.id, "is_super_user": True}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201

    api_client.force_authenticate(user=admin_user)
    response = api_client.get(url)
    assert response.status_code == 200

    api_client.force_authenticate(user=chef_chantier_user)
    response = api_client.get(url)
    assert response.status_code == 403
