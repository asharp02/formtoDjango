# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-31 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GIS_Poster', '0023_auto_20180131_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='Year_range',
            field=models.CharField(default='2017', max_length=200),
        ),
        migrations.AlterField(
            model_name='poster',
            name='PDFPoster',
            field=models.FileField(upload_to='S:/Posters/GIS Posters/<django.db.models.fields.CharField>/PostersComplete<django.db.models.fields.CharField><django.db.models.fields.IntegerField>/<django.db.models.fields.CharField>_<django.db.models.fields.CharField>/<django.db.models.fields.CharField>_<django.db.models.fields.CharField>_<django.db.models.fields.CharField>_<django.db.models.fields.IntegerField>', verbose_name='PDF of Poster'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='Year',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018)]),
        ),
    ]