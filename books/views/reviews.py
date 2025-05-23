from books.serializers import ReviewSerializer, ReviewCardSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
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
    permission_classes = [IsAuthenticated, IsCustomer]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating']

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Review.objects.filter(book_id=book_id).select_related('book', 'reviewer')

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewCardSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        serializer.save(book=book, reviewer=self.request.user)

    def update(self, request, *args, **kwargs):
        review = Review.objects.filter(book_id=self.kwargs['book_id'], reviewer=request.user).first()

        if not review:
            return Response({"detail": "Review not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(review, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        review = Review.objects.filter(book_id=self.kwargs['book_id'],reviewer=request.user).first()

        if not review:
            return Response({"detail": "Review not found."},
                            status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)