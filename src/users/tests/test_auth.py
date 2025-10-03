from django.urls import reverse

import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from src.users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        kwargs.setdefault("username", kwargs.get("email"))
        return User.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def user_with_token(create_user):
    user = create_user(
        email="test@example.com",
        username="test@example.com",
        phone_number="+1234567890",
        password="testpassword",
    )
    refresh = RefreshToken.for_user(user)
    return {
        "user": user,
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@example.com", "testpassword", 200),
        ("test@example.com", "wrongpassword", 401),
        ("unknown@example.com", "testpassword", 401),
    ],
)
def test_login_email(api_client, create_user, email, password, status_code):
    create_user(email="test@example.com", username="test@example.com", password="testpassword")
    url = reverse("login-email")
    data = {"email": email, "password": password}
    response = api_client.post(url, data, format="json")

    assert response.status_code == status_code
    if status_code == 200:
        assert "access" in response.data
        assert "refresh" in response.data
        assert "id" in response.data
        assert "user_type" in response.data
    else:
        assert "access" not in response.data
        assert "refresh" not in response.data


@pytest.mark.django_db
@pytest.mark.parametrize(
    "phone,password,status_code",
    [
        ("+1234567890", "testpassword", 200),
        ("+1234567890", "wrongpassword", 401),
        ("+9876543210", "testpassword", 401),
    ],
)
def test_login_phone(api_client, create_user, phone, password, status_code):
    create_user(
        email="test@example.com",
        username="test@example.com",
        phone_number="+1234567890",
        password="testpassword",
    )
    url = reverse("login-phone")
    data = {"phone_number": phone, "password": password}
    response = api_client.post(url, data, format="json")

    assert response.status_code == status_code
    if status_code == 200:
        assert "access" in response.data
        assert "refresh" in response.data
    else:
        assert "access" not in response.data
        assert "refresh" not in response.data


@pytest.mark.django_db
def test_token_refresh(api_client, user_with_token):
    url = reverse("token-refresh")
    data = {"refresh": user_with_token["refresh"]}
    response = api_client.post(url, data, format="json")

    assert response.status_code == 200
    assert "access" in response.data
