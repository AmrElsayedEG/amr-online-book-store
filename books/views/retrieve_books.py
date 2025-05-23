from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from utils import IsCustomer
from books.serializers import BookSerializer
from books.models import Book

class RetrieveBookAPIView(RetrieveAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsCustomer,)
    lookup_field = 'id'