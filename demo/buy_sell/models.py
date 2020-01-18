# Create your models here.
from django.db import models

from django.contrib.auth.models import User

LANGUAGES = [
    ("fr-CA", "French (Canada)"),
    ("fr", "French"),
    ("es", "Spanish"),
    ("ru", "Russian")
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(max_length=8, choices=LANGUAGES)

    def __str__(self):
        return  f"{self.user.username} <{self.user.email}>"


class Ad(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.TextField()
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title[:32]} - {self.author.user.username} - {self.posted}"

