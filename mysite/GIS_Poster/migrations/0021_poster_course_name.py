# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-26 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GIS_Poster', '0020_course_course_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='Course_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GIS_Poster.Course', verbose_name='GIS Course'),
            preserve_default=False,
        ),
    ]