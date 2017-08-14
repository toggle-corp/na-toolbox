from django.db import models
from django.template.defaultfilters import slugify


class Format(models.Model):
    title = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons',
                            null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class ToolList(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(default=None, null=True, blank=True,
                            editable=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ToolList, self).save(*args, **kwargs)

    class Meta:
        ordering = ['order']


class Category(models.Model):
    title = models.CharField(max_length=250)
    tool_list = models.ForeignKey(ToolList)
    order = models.CharField(default='', max_length=10, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order']


class Tool(models.Model):
    category = models.ForeignKey(Category)

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    format = models.ForeignKey(Format, default=None, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True)
    thumbnail = models.FileField(upload_to='thumbnails',
                                 null=True, blank=True, default=None)
    organization = models.CharField(max_length=150, blank=True)

    order = models.CharField(default='', max_length=10, blank=True)

    tool_type = models.CharField(default='', max_length=100, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


# EOF
