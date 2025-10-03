from django.urls import include
from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from src.users.controllers.UserViewSet import UpdatePasswordView
from src.users.controllers.UserViewSet import UpdateUserInfoView
from src.users.controllers.UserViewSet import UserIdentityView
from src.users.controllers.UserViewSet import UserObtainPairView


router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("identity/", UserIdentityView.as_view(), name="user-identity"),
    path(
        "login-email/",
        UserObtainPairView.as_view(),
        name="login-email",
    ),
    path(
        "token-refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),
    path("update-password/", UpdatePasswordView.as_view(), name="update-password"),
    path("update-info/", UpdateUserInfoView.as_view(), name="update-user-info"),
]
