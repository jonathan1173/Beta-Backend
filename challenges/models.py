from django.db import models
from access.models import User  # Importación de User desde la app Access

class Challenge(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    difficulty = models.PositiveSmallIntegerField()
    test = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class UserChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    progress = models.TextField(blank=True, null=True)
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"
