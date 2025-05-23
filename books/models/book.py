from django.db import models
from .author import Author

def books_cover(instance, filename):
    return f"books_cover/{filename}"

class Book(models.Model):
    # We could use ULID for more secure ids but for simplicity we will use normal incremental id

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_books')
    cover = models.ImageField(upload_to=books_cover)
    description = models.TextField()
    publish_year = models.SmallIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        indexes = [
            models.Index(fields=['publish_year']),
        ]

    def __str__(self) -> str:
        return self.title