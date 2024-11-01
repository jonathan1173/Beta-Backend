from django.db import models
from access.models import User  # Importación de User desde la app Access

class Book(models.Model):
    title = models.TextField()
    author = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    in_cart = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
