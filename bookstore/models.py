from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}-{self.title}'


class Category(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tag}'
