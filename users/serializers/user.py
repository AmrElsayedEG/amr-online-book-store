from rest_framework import serializers
from users.models import User

class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)