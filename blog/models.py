from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def upload_image(self, _):
    return f'posts/{self.slug}/{self.id}'


class Blog(models.Model):
    STATUS_DRAFT_OPTION = 'draft'
    STATUS_PUBLISHED_OPTION = 'published'

    STATUS_CHOICE_OPTION = (
        (STATUS_DRAFT_OPTION, 'Draft'),
        (STATUS_PUBLISHED_OPTION, 'Published'),
    )

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Blog.STATUS_PUBLISHED_OPTION)

    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categories', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='authors', null='anonymous')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    slug = models.CharField(max_length=90, )
    image = models.ImageField(default='posts/default.jpg', upload_to=upload_image)
    visible = models.BooleanField(default=True)
    status = models.CharField(max_length=10, default=STATUS_DRAFT_OPTION, choices=STATUS_CHOICE_OPTION)
    objects = models.Manager()
    published_objects = NewManager()

    class Meta:
        ordering = ('-published_at',)
        verbose_name_plural = 'Post'

    def __str__(self):
        return f'{self.id} {self.title}'


class Category(models.Model):
    tag = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.tag}'
