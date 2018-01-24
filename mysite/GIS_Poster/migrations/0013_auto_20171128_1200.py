# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 17:00
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('GIS_Poster', '0012_auto_20171128_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='SchoolName',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SAS', 'School of Arts and Sciences'), ('SE', 'School of Engineering'), ('Fletcher', 'The Fletcher School of Law and Diplomacy'), ('Friedman', 'Gerald J. and Dorothy R. Friedman School of Nutrition Science and Policy'), ('Cummings', 'Cummings School of Veterinary Medicine'), ('Med', 'School of Medicine'), ('Dental', 'School of Dental Medicine'), ('Feinstein', 'Feinstein International Center'), ('PubSafety', 'Public Safety'), ('TIE', 'Tufts Institute for the Environment'), ('Other', 'Other')], max_length=74, verbose_name='School Name\n Which School is the student housed in? Choose all that apply'),
        ),
    ]
