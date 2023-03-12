from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from markdown import Markdown


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'avatar/user_{0}/{1}'.format(instance.author.id, filename)


class Avatar(models.Model):

    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='avatars')
    content = models.ImageField(upload_to=user_directory_path)


class Category(models.Model):
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='category'
    )
    category = models.CharField(max_length=30, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category


class Tag(models.Model):
    text = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text


class Article(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles')
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles')
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles'
    )

    class Meta:
        ordering = ['-created', ]

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        # toc 是渲染后的目录
        return md_body, md.toc

    def __str__(self):
        return self.title
