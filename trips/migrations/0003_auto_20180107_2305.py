# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20180107_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='locality',
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='meeting_point',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='parent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='photo_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='trip',
            name='num_followers',
            field=models.IntegerField(default=0),
        ),
    ]
