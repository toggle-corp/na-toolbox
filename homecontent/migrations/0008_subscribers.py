# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homecontent', '0007_auto_20170814_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('duty_station', models.CharField(max_length=200)),
            ],
        ),
    ]
