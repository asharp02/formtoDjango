# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_code', models.CharField(max_length=200)),
                ('Course_name', models.CharField(max_length=200)),
                ('Dept_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('StudentName', models.CharField(default=models.CharField(max_length=200, verbose_name='First Name'), max_length=200)),
                ('degree', multiselectfield.db.fields.MultiSelectField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PhD', 'PhD'), ('Faculty/Staff', 'Faculty/Staff'), ('Certificate', 'Certificate')], max_length=47)),
                ('SchoolName', multiselectfield.db.fields.MultiSelectField(choices=[('SAS', 'School of Arts and Sciences'), ('SE', 'School of Engineering'), ('Fletcher', 'The Fletcher School of Law and Diplomacy'), ('Friedman', 'Gerald J. and Dorothy R. Friedman School of Nutrition Science and Policy'), ('Cummings', 'Cummings School of Veterinary Medicine'), ('Med', 'School of Medicine'), ('Dental', 'School of Dental Medicine'), ('Feinstein', 'Feinstein International Center'), ('PubSafety', 'Public Safety'), ('TIE', 'Tufts Institute for the Environment'), ('Other', 'Other')], max_length=74, verbose_name='School Name')),
                ('DepartmentName', multiselectfield.db.fields.MultiSelectField(choices=[('AMER', 'American Studies'), ('ANTH', 'Anthropology'), ('ARC', 'Archaeology'), ('ARCH', 'Architectural Studies'), ('BIO', 'Biology'), ('BIOPSYCH', 'Biopsychology'), ('CD', 'Child Study and Human Development'), ('CHN', 'Chinese'), ('CEE', 'Civil and Environmental Engineering'), ('CLA', 'Classics'), ('CH', 'Community Health'), ('CS', 'Computer Science'), ('CONS', 'Conservation Medicine'), ('EOS', 'Earth and Ocean Studies'), ('ECON', 'Economics'), ('ENG_PHYS', 'Engineering Physics'), ('ENG_SCI', 'Engineering Science'), ('ENG', 'English'), ('ELS', 'Entrepreneurial Leadership'), ('FR', 'French'), ('HIS', 'History'), ('IR', 'International Relations'), ('MATH', 'Mathematics'), ('ME', 'Mechanical Engineering'), ('MUS', 'Music'), ('PJS', 'Peace and Justice Studies'), ('PHIL', 'Philosophy'), ('PHY', 'Physics'), ('PS', 'Political Science'), ('PSY', 'Psychology'), ('PH', 'Public Health'), ('REE', 'Russian and Eastern European Studies'), ('SOC', 'Sociology'), ('SPN', 'Spanish'), ('STATS', 'Statistics'), ('TTS', 'Tufts Technology Services'), ('UEP', 'Urban and Environmental Policy and Planning (UEP'), ('Other', 'Other')], max_length=168, verbose_name="Student's Department(s)")),
                ('Dept_code', models.CharField(default='GIS101', max_length=200)),
                ('Semester', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], max_length=20)),
                ('Year', models.CharField(choices=[('2016', '2016'), ('2017', '2017')], max_length=20)),
                ('FullPosterTitle', models.CharField(max_length=200, verbose_name='Title of GIS Poster?')),
                ('ThemeKeywordL1', multiselectfield.db.fields.MultiSelectField(choices=[('AWB', 'Animal, Wildlife and Biota'), ('AEC', 'Architecture, Engineering and Construction'), ('BC', 'Business and Commercial'), ('CD', 'Community Development'), ('DI', 'Defense and Intelligence'), ('EDU', 'Education'), ('EC', 'Energy and Climate'), ('ER', 'Exposure and Risk'), ('FAC', 'Facilities'), ('FD', 'Finance and Development'), ('GOV', 'Government'), ('HLT', 'Health'), ('HUM', 'Humanities'), ('HA', 'Humanitarian Assistance'), ('INF', 'Infrastructure'), ('NR', 'Natural Resources'), ('NUTR', 'Nutrition'), ('PS', 'Public Safety'), ('REC', 'Recreation'), ('TRS', 'Transportation'), ('WAT', 'Water')], max_length=75, verbose_name='Topic Keyword')),
                ('ThemeKeywordL2', multiselectfield.db.fields.MultiSelectField(choices=[('Air and Atmosphere', 'Air and Atmosphere'), ('Accessibility', 'Accessibility'), ('Agriculture', 'Agriculture'), ('Alternative and Renewable Energy', 'Alternative and Renewable Energy'), ('Animal Health', 'Animal Health'), ('Archeology', 'Archeology'), ('Aviation', 'Aviation'), ('Banking and Financial Services', 'Banking and Financial Services'), ('Building and Landscape Architecture', 'Building and Landscape Architecture'), ('Census', 'Census'), ('City Management', 'City Management'), ('Climate and Weather', 'Climate and Weather'), ('Climate Change', 'Climate Change'), ('Community Advocacy', 'Community Advocacy'), ('Community Analysis', 'Community Analysis'), ('Community Maps', 'Community Maps'), ('Conflict', 'Conflict'), ('Conservation', 'Conservation'), ('Construction', 'Construction'), ('Contamination', 'Contamination'), ('Criminal Justice', 'Criminal Justice'), ('Cultural Resource Management', 'Cultural Resource Management'), ('Disease', 'Disease'), ('Ecology', 'Ecology'), ('Economic Development', 'Economic Development'), ('Elections', 'Elections'), ('Electric Utilities', 'Electric Utilities'), ('EMS and Emergency Calls', 'EMS and Emergency Calls'), ('Emergency Management', 'Emergency Management'), ('Energy', 'Energy'), ('Energy Planning', 'Energy Planning'), ('Engineering and Design', 'Engineering and Design'), ('Environmental Justice', 'Environmental Justice'), ('Environmental Management', 'Environmental Management'), ('Federal Agencies', 'Federal Agencies'), ('Fire Management', 'Fire Management'), ('Fire Rescue', 'Fire Rescue'), ('Fisheries', 'Fisheries'), ('Flood Management', 'Flood Management'), ('Food Access', 'Food Access'), ('Food Deserts', 'Food Deserts'), ('Food Insecurity', 'Food Insecurity'), ('Food Production', 'Food Production'), ('Forestry', 'Forestry'), ('Gentrification', 'Gentrification'), ('Geosciences', 'Geosciences'), ('Groundwater', 'Groundwater'), ('Hazard management', 'Hazard management'), ('Health Systems', 'Health Systems'), ('Highways and Roads', 'Highways and Roads'), ('History', 'History'), ('Homeland Security', 'Homeland Security'), ('Hospitals', 'Hospitals'), ('Housing', 'Housing'), ('Human Security', 'Human Security'), ('Human Services', 'Human Services'), ('Humanitarian Aid and Relief', 'Humanitarian Aid and Relief'), ('Hydraulic Engineering', 'Hydraulic Engineering'), ('Intelligence', 'Intelligence'), ('International Development', 'International Development'), ('Land Administration', 'Land Administration'), ('Law Enforcement', 'Law Enforcement'), ('Local Government', 'Local Government'), ('Location Based Services', 'Location Based Services'), ('Manufacturing', 'Manufacturing'), ('Medicine', 'Medicine'), ('Military Operations', 'Military Operations'), ('Mining', 'Mining'), ('National Security', 'National Security'), ('Natural Disasters', 'Natural Disasters'), ('Oceans and Maritime', 'Oceans and Maritime'), ('Operations and Maintenance', 'Operations and Maintenance'), ('Parks and Natural Resources', 'Parks and Natural Resources'), ('Petroleum and Fossil Fuels', 'Petroleum and Fossil Fuels'), ('Physical Activity', 'Physical Activity'), ('Pipeline and Gas Utilities', 'Pipeline and Gas Utilities'), ('Policy', 'Policy'), ('Pollution', 'Pollution'), ('Poverty Mapping', 'Poverty Mapping'), ('Public Health', 'Public Health'), ('Public Transit', 'Public Transit'), ('Public Works', 'Public Works'), ('Railways', 'Railways'), ('Real Estate', 'Real Estate'), ('Redistricting', 'Redistricting'), ('Regional Planning', 'Regional Planning'), ('Retail', 'Retail'), ('Risk Assessment', 'Risk Assessment'), ('Safety and Security', 'Safety and Security'), ('Schools', 'Schools'), ('Sea Level Rise', 'Sea Level Rise'), ('Social Inequality', 'Social Inequality'), ('State Government', 'State Government'), ('Storm Water', 'Storm Water'), ('Subsidized Housing', 'Subsidized Housing'), ('Surveying', 'Surveying'), ('Sustainability', 'Sustainability'), ('Telecommunications', 'Telecommunications'), ('Universities and Colleges', 'Universities and Colleges'), ('Urban Planning', 'Urban Planning'), ('Urbanization', 'Urbanization'), ('Wastewater', 'Wastewater'), ('Water Management', 'Water Management'), ('Water Quality', 'Water Quality'), ('Water Quantity', 'Water Quantity'), ('Water Resources', 'Water Resources'), ('Wildlife Management', 'Wildlife Management')], max_length=1741, verbose_name='Sub-Topic Keyword')),
                ('ThemeKeywordL3', multiselectfield.db.fields.MultiSelectField(choices=[('Best Path - Least Cost', 'Best Path - Least Cost'), ('Change Detection', 'Change Detection'), ('Hydro Analysis', 'Hydro Analysis'), ('Needs Analysis', 'Needs Analysis'), ('Network Analysis', 'Network Analysis'), ('Proximity Analysis', 'Proximity Analysis'), ('Remote Sensing', 'Remote Sensing'), ('Statistics/Spatial Statistics', 'Statistics/Spatial Statistics'), ('Suitability Analysis', 'Suitability Analysis'), ('Thematic Mapping', 'Thematic Mapping'), ('Vulnerability Analysis', 'Vulnerability Analysis')], max_length=211, verbose_name='Methodological Keyword')),
                ('PlaceKeywordGeonames', models.CharField(max_length=200, verbose_name='Place Keywords - Where is your GIS project located?')),
                ('SDrivePathway', models.CharField(default='pass', max_length=200)),
                ('image', models.FileField(upload_to='images')),
                ('ReleaseForm', models.BooleanField(verbose_name='Website Release Form')),
                ('ThumbnailName', models.CharField(default='pass', max_length=200)),
                ('ThumbnailPath', models.CharField(default='pass', max_length=200)),
                ('PosterPath', models.CharField(default='pass', max_length=200)),
                ('PosterWinner', models.BooleanField(default='False', verbose_name='Poster Winner')),
                ('Approved', models.CharField(default='', max_length=15)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GIS_Poster.Course')),
            ],
        ),
        migrations.CreateModel(
            name='PosterMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Winner_name', models.CharField(max_length=200)),
                ('poster_approved', models.CharField(max_length=15)),
            ],
        ),
    ]
