# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0036_remove_profile_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null='False', upload_to='static/profile/'),
        ),
    ]