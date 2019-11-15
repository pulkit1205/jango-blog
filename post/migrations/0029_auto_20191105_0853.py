# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_auto_20191105_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null='True', upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
