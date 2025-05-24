from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from utils import IsCustomer, CustomPageNumberPagination
from books.serializers import BookCardSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from books.models import Book

class ListBooksAPIView(ListAPIView):
    """
    API view to list all active books for authenticated customers.

    This view provides a paginated list of books that are marked as active.
    It supports filtering by `publish_year` and searching by `title` and author's name.
    """
    serializer_class = BookCardSerializer
    permission_classes = (IsAuthenticated, IsCustomer,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ('publish_year',)
    search_fields = ['title', 'author__author_name',]
    pagination_class = CustomPageNumberPagination
    
    def get_queryset(self):
        
        return Book.objects.filter(is_active=True).select_related('author')