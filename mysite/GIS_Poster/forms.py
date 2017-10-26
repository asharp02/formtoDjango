from django import forms
from .models import Poster

COURSE_CHOICES = (('GIS 101/ ENV 107/ INTR 81: Introduction to Geographic Information Systems', 
			'GIS 101/ ENV 107/ INTR 81: Introduction to Geographic Information Systems'),
		  ('UEP 0232: Intro to GIS- GIS for Urban Analysis',
		  	'UEP 0232: Intro to GIS- GIS for Urban Analysis'),
		  ('GIS 102/ UEP 29422/ ENV 197: Advanced Geographic Information Systems',
		  	'GIS 102/ UEP 29422/ ENV 197: Advanced Geographic Information Systems'),
		  ('Fletcher DHP P207: GIS for International Applications',
		  	'Fletcher DHP P207: GIS for International Applications'),
		  ('CEE 187: Geographic Information Systems',
		  	'CEE 187: Geographic Information Systems'),
		  ('NUTR 231: Fundamentals of GIS for Food, Agriculture, and Environmental Applications',
		  	'NUTR 231: Fundamentals of GIS for Food, Agriculture, and Environmental Applications'),
		  ('EOS 104: Geological Applications of GIS',
		  	'EOS 104: Geological Applications of GIS'),
		  ('CEE 194A: Introduction to Remote Sensing',
		  	'CEE 194A: Introduction to Remote Sensing'),
		  ('PH 0262: GIS for Public Health',
		  	'PH 0262: GIS for Public Health'),
		  ('MCM 1009: GIS for Conservation Medicine',
		  	'MCM 1009: GIS for Conservation Medicine'),
		  ('Not enrolled in a GIS Course',
		  	'Not enrolled in a GIS Course'),
		  ('Other', 'Other')
		  )

class PosterCreateForm(forms.ModelForm):

	class Meta: 
		model = Poster
		fields = {'first_name', 'last_name', 'degree', 'SchoolName',
					'DepartmentName', 'Course', 'Semester', 'Year',
					'FullPosterTitle', 'ThemeKeywordL1', 'ThemeKeywordL2',
					'ThemeKeywordL3', 'PlaceKeywordGeonames', 'image',
					'ReleaseForm'}
	Course = forms.TypedChoiceField(choices=COURSE_CHOICES, widget=forms.RadioSelect())

	# last_name = models.CharField(max_length = 200)
	# StudentName = models.CharField(max_length = 200)
	# degree = MultiSelectField(choices=DEGREE_CHOICES)
	# SchoolName = MultiSelectField(choices=SCHOOL_CHOICES)
	# DepartmentName = MultiSelectField(choices=DEPARTMENT_CHOICES, max_choices=1)
	# Course = models.CharField(max_length=200, choices=COURSE_CHOICES)
	# Semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
	# Year = models.CharField(max_length=20, choices=YEAR_CHOICES)
	# FullPosterTitle = models.CharField(max_length=200)
	# ThemeKeywordL1 = MultiSelectField(choices=TOPIC_CHOICES)
	# ThemeKeywordL2 = MultiSelectField(choices=SUBTOPIC_CHOICES)
	# ThemeKeywordL3 = MultiSelectField(choices=METHOD_CHOICES)
	# PlaceKeywordGeonames = models.CharField(max_length=200) #dont know if this should be an integerfield or charfield for multiple geonames
	# SDrivePathway = models.CharField(max_length=200)
	# image = models.FileField(upload_to='images')
	# ReleaseForm = models.BooleanField()
	# ThumbnailName = models.CharField(max_length=200)
	# ThumbnailPath = models.CharField(max_length=200)
	# PosterPath = models.CharField(max_length=200)