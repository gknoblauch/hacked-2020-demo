# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

LANGUAGES = [
    ("en", "English"),
    ("fr-CA", "French (Canada)"),
    ("fr", "French"),
    ("es", "Spanish"),
    ("ru", "Russian"),
]

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    preferred_language = models.CharField(max_length=8, choices=LANGUAGES)

    def __str__(self):
        return  f"{self.user.username} <{self.user.email}>"

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.user_profile.save()


class Ad(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.TextField()
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title[:32]} - {self.author.user.username} - {self.posted}"

