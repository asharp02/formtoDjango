# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GIS_Poster', '0029_auto_20180319_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poster',
            name='release_signature',
        ),
    ]
