from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from Authentication.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("email", "phone", "password", "firstname", "lastname", "role",
                  "bonus_balance", "balance", "rating", "is_active",
                  "is_staff",)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)