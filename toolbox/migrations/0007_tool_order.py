# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0006_tool_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
