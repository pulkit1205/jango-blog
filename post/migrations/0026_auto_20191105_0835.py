# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 08:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_remove_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='image',
            new_name='Image',
        ),
    ]
