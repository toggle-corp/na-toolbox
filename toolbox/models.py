from django.db import models


class Format(models.Model):
    title = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons',
            null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class ToolList(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=250)
    tool_list = models.ForeignKey(ToolList)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Tool(models.Model):
    category = models.ForeignKey(Category)

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    format = models.ForeignKey(Format, default=None, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True)
    thumbnail = models.FileField(upload_to='thumbnails',
            null=True, blank=True, default=None)
    fields = models.TextField(default='{}')

    def __str__(self):
        return self.title


# EOF
