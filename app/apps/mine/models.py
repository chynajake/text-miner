from django.db import models
from apps.authentication.models import User


class Text(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def short_text(self):
        return self.content[:40]

    def __str__(self):
        return '{} - {}'.format(self.pk, self.creator.email)