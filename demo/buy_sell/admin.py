from django.contrib import admin

# Register your models here.
from .models import Ad, Profile

admin.site.register(Ad)
admin.site.register(Profile)

