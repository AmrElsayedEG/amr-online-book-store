from rest_framework import serializers
from books.models import Author

class AuthorCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('author_name', 'picture',)

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        exclude = ('created_at',)