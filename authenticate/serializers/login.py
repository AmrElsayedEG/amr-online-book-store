from rest_framework import serializers
from users.models import User
from django.utils.translation import gettext_lazy as _

class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer for handling user login.

    This serializer validates a user's email and password credentials.
    If valid and the user is active, the authenticated user instance is added to the validated data.
    """

    error_msg = {
        "login" : {
            "error" : _("Invalid Credentials"),
        },
        "not_active" : {
            "error" : _("This account is not activated, Please contact the support."),
        },
    }

    email = serializers.CharField(help_text="Enter email")
    password = serializers.CharField(help_text="Enter password")

    class Meta:
        model = User
        fields = ('email', 'password',)

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email']).last()

        if not user or not user.check_password(attrs['password']):
            raise serializers.ValidationError(self.error_msg['login'])

        if not user.is_active:
            raise serializers.ValidationError(self.error_msg['not_active'])

        attrs['user'] = user

        return attrs