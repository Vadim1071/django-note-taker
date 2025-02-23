from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", verbose_name="теги", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'заметки'
        verbose_name = 'заметка'

class Application(models.Model):
    class Type(models.IntegerChoices):
        REFERENCE = 0
        IMAGE = 1
        VIDEO = 2

    application_type = models.IntegerField(
        choices=Type.choices,
        null=False
    )

    application_file = models.FileField(
        null=True, blank=True,
        upload_to='uploads/%Y/%m/%d/',
    )


class Tag(models.Model):
    title = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.ManyToManyField(Note, verbose_name="заметки", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'теги'
        verbose_name = 'тег'


class Folder(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    parent_folder = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def notes(self):
        return Note.objects.filter(folder=self)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'папки'
        verbose_name = 'папка'
