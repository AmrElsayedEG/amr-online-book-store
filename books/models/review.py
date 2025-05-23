from django.db import models
from django.conf import settings
from .book import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):

    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'