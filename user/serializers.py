from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label="Пароль", max_length=20, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)
