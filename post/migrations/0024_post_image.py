# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null='True', upload_to='proimages/'),
        ),
    ]
