# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-04 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20191101_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
