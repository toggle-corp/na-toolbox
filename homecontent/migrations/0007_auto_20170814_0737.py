# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 07:37
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homecontent', '0006_auto_20170814_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='keylink',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]