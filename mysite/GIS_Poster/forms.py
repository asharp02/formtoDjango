from django import forms
from .models import Poster, Course


COURSE_CHOICES = (('GIS101', 
			'GIS 101/ ENV 107/ INTR 81: Introduction to Geographic Information Systems'),
		  ('UEP232',
		  	'UEP 0232: Intro to GIS- GIS for Urban Analysis'),
		  ('GIS 102',
		  	'GIS 102/ UEP 29422/ ENV 197: Advanced Geographic Information Systems'),
		  ('DHP207',
		  	'Fletcher DHP P207: GIS for International Applications'),
		  ('CEE187',
		  	'CEE 187: Geographic Information Systems'),
		  ('NUTR0231',
		  	'NUTR 231: Fundamentals of GIS for Food, Agriculture, and Environmental Applications'),
		  ('EOS104',
		  	'EOS 104: Geological Applications of GIS'),
		  ('CEE194',
		  	'CEE 194A: Introduction to Remote Sensing'),
		  ('PH262',
		  	'PH 0262: GIS for Public Health'),
		  ('MCM1009',
		  	'MCM 1009: GIS for Conservation Medicine'),
		  ('Not enrolled in a GIS Course',
		  	'Not enrolled in a GIS Course'),
		  ('Other', 'Other')
		  )
SEMESTER_CHOICES = (('Spring', 'Spring'),
					('Summer', 'Summer'),
					('Fall', 'Fall'))

YEAR_CHOICES = (('2016', '2016'),
				('2017', '2017'))



class PosterCreateForm(forms.ModelForm):
	class Meta: 
		model = Poster
		fields = ['first_name', 'last_name', 'degree', 'SchoolName',
					'DepartmentName', 'Course_name', 'Semester', 'Year',
					'FullPosterTitle', 'ThemeKeywordL1', 'ThemeKeywordL2',
					'ThemeKeywordL3', 'PlaceKeywordGeonames', 'image',
					'ReleaseForm']
	#Course = forms.TypedChoiceField(choices=COURSE_CHOICES, widget=forms.RadioSelect())
	#Dept_code = Course.objects.get(id='1')
	Semester = forms.TypedChoiceField(choices=SEMESTER_CHOICES, widget=forms.RadioSelect())
	Year = forms.TypedChoiceField(choices=YEAR_CHOICES, widget=forms.RadioSelect())
	#ReleaseForm = forms.TypedChoiceField(choices=COURSE_CHOICES, widget=forms.RadioSelect())

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['Course_name', 'Course_code', 'Dept_code']