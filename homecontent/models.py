from django.db import models
from tinymce.models import HTMLField


class Introduction(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    background_image = models.FileField(blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class DownloadSection(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Download(models.Model):
    section = models.ForeignKey(DownloadSection)
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    file = models.FileField(upload_to='downloads',
                            null=True, blank=True, default=None)
    thumbnail = models.FileField(upload_to='download_thumbnails',
                                 null=True, blank=True, default=None)
    enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class KeyLink(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    url = models.CharField(max_length=300, blank=True)
    enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Highlight(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    url = models.CharField(max_length=300, blank=True)
    preview = models.FileField(upload_to='highlight_previews',
                               null=True, blank=True, default=None)
    enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
