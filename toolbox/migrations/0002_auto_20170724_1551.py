# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.FileField(blank=True, default=None, null=True, upload_to='icons')),
            ],
        ),
        migrations.AlterField(
            model_name='tool',
            name='format',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='toolbox.Format'),
        ),
    ]