from rest_framework import serializers

from src.users.models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "phone_number", "image"]
        read_only_fields = ["id"]
