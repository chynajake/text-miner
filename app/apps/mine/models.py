from django.db import models
from apps.authentication.models import User


class Text(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def short_text(self):
        return '{}...'.format(self.content[:40])

    def __str__(self):
        return '{} - {}'.format(self.pk, self.creator.email)


class ModeratedText(models.Model):
    content = models.TextField()
    raw_text = models.ForeignKey(Text, on_delete=models.CASCADE)
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def short_text(self):
        return '{}...'.format(self.content[:40])

    def __str__(self):
        return '{} - {}'.format(self.pk, self.moderator.email)