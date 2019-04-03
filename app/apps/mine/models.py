from django.db import models
from apps.authentication.models import User


class Text(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)