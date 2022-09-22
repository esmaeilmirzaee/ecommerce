from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} {self.title}'
