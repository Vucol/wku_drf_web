from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
def textbook_path(instance, filename):
    filename = '{0} - {1} -{2}-'.format(
        instance.textbook.author,
        instance.textbook.title,
        instance.textbook.edition)
    # file will be uploaded to MEDIA_ROOT/textbook/<filename>
    return 'textbook/{0}'.format(filename)


def syllabus_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/syllabus/<filename>
    return 'syllabus/{0}'.format(filename)


class BookTag(models.Model):
    text = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text


class Textbook(models.Model):
    CHINESE = 'CN'
    ENGLISH = 'EN'
    LANGUAGE_CHOICES = [
        (CHINESE, 'Chinese'),
        (ENGLISH, 'English'),
    ]
    uploader = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    upload = models.FileField(upload_to=textbook_path)
    posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    edition = models.CharField(max_length=10)
    publisher = models.CharField(max_length=50)
    year = models.IntegerField()
    ISBN = models.BigIntegerField()
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
    )
    # 不同翻译版本的自关联关系
    translated = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='version',
    )
    tags = models.ManyToManyField(
        BookTag,
        blank=True,
        related_name='textbooks'
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    subject = models.CharField(max_length=100)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    credit = models.IntegerField(default=0)
    description = models.TextField()
    requisites = models.TextField(null=True, blank=True,default=None)
    offered = models.TextField(null=True, blank=True,default=None)
    # 多对多关系，textbook 被放在 Course 当中
    textbook = models.ManyToManyField(
        Textbook,
        blank=True,
        related_name='courses'
    )

    class Meta:
        unique_together = [['subject', 'number']]
        ordering = ['subject', 'number']

    def __str__(self):
        return self.subject + ' ' + str(self.number) + ' ' + self.name


class Syllabus(models.Model):
    uploader = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    upload = models.FileField(upload_to=syllabus_path)
    title = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    professor = models.CharField(max_length=50)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='syllabuses'
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
