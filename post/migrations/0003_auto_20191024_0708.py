# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-24 07:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
