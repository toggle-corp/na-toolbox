# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('field_support', '0002_auto_20170910_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fieldsupport',
            old_name='join_activity',
            new_name='joint_activity',
        ),
    ]