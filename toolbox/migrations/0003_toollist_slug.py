# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0002_auto_20170724_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='toollist',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
    ]
