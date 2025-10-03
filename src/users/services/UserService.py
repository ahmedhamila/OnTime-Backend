from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from src.users.models.User import User
from src.users.serializers.UserSerializer import UserSerializer


class UserService:
    @classmethod
    def get_user_identity(cls, user, request):
        if not user or not user.is_authenticated:
            raise APIException(detail="Invalid user")

        return Response(UserSerializer(user, context={"request": request}).data)

    @classmethod
    def update_password(cls, user, data):

        current_password = data.get("current_password")
        new_password = data.get("new_password")

        if not user.check_password(current_password):
            raise ValidationError(detail="Current password is incorrect")

        if not new_password:
            raise ValidationError(detail="New password cannot be empty")

        user.set_password(new_password)
        user.save()

        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)

    @classmethod
    def update_user_info(cls, user, data, files):
        """
        Update basic user info (first name, last name, email, phone, image).
        """
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")
        phone_number = data.get("phoneNumber")
        image = files.get("image") if files else None

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name

        if email:
            existing_user = User.objects.filter(email=email).exclude(pk=user.pk).first()
            if existing_user:
                raise ValidationError(detail="This email is already in use")
            user.email = email

        if phone_number:
            existing_user = (
                User.objects.filter(phone_number=phone_number).exclude(pk=user.pk).first()
            )
            if existing_user:
                raise ValidationError(detail="This phone number is already in use")
            user.phone_number = phone_number

        if image:
            user.image = image

        user.save()

        return Response(UserSerializer(user).data)
