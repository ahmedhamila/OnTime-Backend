from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from src.users.serializers.UserObtainPairSerializer import UserObtainPairSerializer
from src.users.services.UserService import UserService


class UserObtainPairView(TokenObtainPairView):
    serializer_class = UserObtainPairSerializer


class UserIdentityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return UserService.get_user_identity(request.user, request)


class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        return UserService.update_password(request.user, request.data)


class UpdateUserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request):
        return UserService.update_user_info(request.user, request.data, request.FILES)
