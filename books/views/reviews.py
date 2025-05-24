from books.serializers import ReviewSerializer, ReviewCardSerializer
from rest_framework.permissions import IsAuthenticated
from utils import IsCustomer, CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from books.models import Review, Book
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

class ReviewViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """
    A viewset to manage book reviews for authenticated customers.

    This viewset provides the ability to list, create, update, and delete
    reviews related to a specific book. Reviews are filtered by book ID 
    and optionally by rating. Only the reviewer who created the review can
    update or delete it.
    """
    permission_classes = [IsAuthenticated, IsCustomer]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating']
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Review.objects.filter(book_id=book_id).select_related('book', 'reviewer')

    def get_serializer_class(self):
        """
        This function differentiate between List Reviews and other methods
        In case of GET then we will use 'ReviewCardSerializer' which will have extra fields in the serializer
        If it's POST, PUT then will use 'ReviewSerializer' fields.
        """
        if self.action == 'list':
            return ReviewCardSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        serializer.save(book=book, reviewer=self.request.user)

    def update(self, request, *args, **kwargs):
        """
        This function handles the PUT request to update the ratirng, If user doesn't have rating then will raise error with 404
        If user has review, Then will update it and save and return it back to the user.
        Only user's review will be updated.
        """
        review = Review.objects.filter(book_id=self.kwargs['book_id'], reviewer=request.user).first()

        if not review:
            return Response({"detail": "Review not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(review, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        This function handles the DELETE request to delete the ratirng, If user doesn't have rating then will raise error with 404
        If user has review, Then will delete it and return 204.
        Only user's review will be deleted.
        """
        review = Review.objects.filter(book_id=self.kwargs['book_id'],reviewer=request.user).first()

        if not review:
            return Response({"detail": "Review not found."},
                            status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)