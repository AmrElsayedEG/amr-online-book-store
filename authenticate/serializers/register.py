from rest_framework import serializers
from users.models import User
import logging

logger = logging.getLogger(__name__)

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.

    This serializer handles the creation of a new user by accepting
    basic user information including a plain text password. The password is hashed
    before saving the user instance to the database.

    Meta:
        model (User): The user model associated with the serializer.
        fields (tuple): Fields required for registration.
        extra_kwargs (dict): Ensures the password is write-only.
    """

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
