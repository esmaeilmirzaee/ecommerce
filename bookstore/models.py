from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}-{self.title}'


class Category(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tag}'


class Profile(models.Model):
    ROLE_CHOICES = (
        (1, 'Customer'),
        (2, 'Supplier'),
        (3, 'Admin'),
        (4, 'SuperAdmin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True, default=1)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return '%s' % self.user.email

    def __str__(self):
        return f'{self.user.username}'
