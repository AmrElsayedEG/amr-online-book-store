from rest_framework import serializers
from books.models import Book
from .author import AuthorCardSerializer, AuthorSerializer

class BookCardSerializer(serializers.ModelSerializer):
    author = AuthorCardSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'cover', 'publish_year',)

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        exclude = ('is_active', 'created_at',)