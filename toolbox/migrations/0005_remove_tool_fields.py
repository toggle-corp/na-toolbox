# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0004_auto_20170730_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='fields',
        ),
    ]
