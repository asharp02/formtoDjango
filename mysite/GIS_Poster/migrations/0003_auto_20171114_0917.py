# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GIS_Poster', '0002_auto_20171114_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIS_Poster.Course'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='Dept_code',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIS_Poster.Course'), max_length=200),
        ),
    ]
