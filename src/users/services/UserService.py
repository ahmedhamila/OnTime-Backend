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
            raise APIException(detail="Utilisateur invalide")

        return Response(UserSerializer(user, context={"request": request}).data)

    @classmethod
    def update_password(cls, user, data):

        current_password = data.get("current_password")
        new_password = data.get("new_password")

        if not user.check_password(current_password):
            raise ValidationError(detail="Le mot de passe actuel est incorrect")

        if not new_password:
            raise ValidationError(detail="Le nouveau mot de passe ne peut pas être vide")

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Mot de passe mis à jour avec succès"}, status=status.HTTP_200_OK
        )

    @classmethod
    def update_user_info(cls, user, data, files):

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
                raise ValidationError(detail="Cet e-mail est déjà utilisé")
            user.email = email

        if phone_number:
            existing_user = (
                User.objects.filter(phone_number=phone_number).exclude(pk=user.pk).first()
            )
            if existing_user:
                raise ValidationError(detail="Ce numéro de téléphone est déjà utilisé")
            user.phone_number = phone_number

        if image:
            user.image = image

        user.save()

        return Response(UserSerializer(user).data)
