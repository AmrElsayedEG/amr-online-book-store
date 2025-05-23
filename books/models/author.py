from django.db import models

def authors_picture(instance, filename):
    return f"authors_picture/{filename}"

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    picture = models.ImageField(upload_to=authors_picture)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'author'

    def __str__(self) -> str:
        return self.author_name