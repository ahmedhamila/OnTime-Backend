from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return super().get_token(user)

    def validate(self, attrs):

        super().validate(attrs)
        refresh = self.get_token(self.user)
        access = refresh.access_token

        response_data = {
            "refresh": str(refresh),
            "access": str(access),
        }

        return response_data
