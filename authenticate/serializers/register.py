from rest_framework import serializers
from users.models import User
import logging

logger = logging.getLogger(__name__)

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password',)
        extra_kwargs = {'password' : {'write_only':True}}

    def create(self, validated_data):
        password = validated_data.get('password')

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        return user
