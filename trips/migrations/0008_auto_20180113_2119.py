# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 21:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20180113_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]