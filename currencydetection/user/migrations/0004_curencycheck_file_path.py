# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-24 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20181024_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='curencycheck',
            name='file_path',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]