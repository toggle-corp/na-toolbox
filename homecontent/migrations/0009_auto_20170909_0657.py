# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homecontent', '0008_subscribers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]