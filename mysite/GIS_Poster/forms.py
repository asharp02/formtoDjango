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

RELEASE_CHOICES = [('Yes', 'Yes'),
					('No', 'No')]

class PosterCreateForm(forms.ModelForm):
	class Meta: 
		model = Poster
		fields = ['first_name', 'last_name', 'degree', 'SchoolName',
					'DepartmentName', 'Course_name', 'Semester', 'Year',
					'FullPosterTitle', 'ThemeKeywordL1', 'ThemeKeywordL2',
					'ThemeKeywordL3', 'PlaceKeywordGeonames', 'PDFPoster',
					'release_form']
		help_texts = {
			'SchoolName': 'Which School is the student housed in? Choose all that apply',
			'DepartmentName': 'Which department is the student in? If your department is not listed, please enter it below.',
			'Course_name' : 'Which GIS Course is the student currently enrolled in?',
			'FullPosterTitle' : 'Full name of GIS poster title. Please include the sub-title, if applicable',
			'ThemeKeywordL1' : 'This is a keyword to explain the overall topic of the student\'s GIS Project - Choose as many as you find appropriate.',
			'ThemeKeywordL2' : 'This is a more detailed keyword about the student\'s GIS project - Choose all that apply!',
			'ThemeKeywordL3' : 'Select the methodological keyword for this GIS Analysis - Choose all that apply.',
			'PlaceKeywordGeonames' : 'You must use Geonames to get this code. A Lab Assistant will help you with this field! Lab Assistants, follow the directions on accessing Geonames in directions, please navigate to: http://www.geonames.org',
		}
	release_form = forms.TypedChoiceField(choices=RELEASE_CHOICES, widget=forms.RadioSelect(), help_text='The student has signed the website release form?')
	Course_name = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.RadioSelect(), initial=Course.objects.all()[0], help_text='Which GIS Course is the student currently enrolled in?')
	Semester = forms.TypedChoiceField(choices=SEMESTER_CHOICES, widget=forms.RadioSelect(), help_text='Which Semester was the student enrolled in GIS?')
	Year = forms.TypedChoiceField(choices=YEAR_CHOICES, widget=forms.RadioSelect(), help_text='What year was the student enrolled in GIS')
	
	#Course_name = forms.TypedChoiceField(choices=YEAR_CHOICES, widget=forms.RadioSelect())

	#ReleaseForm = forms.TypedChoiceField(choices=COURSE_CHOICES, widget=forms.RadioSelect())

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['Course_name', 'Course_code', 'Dept_code']
		
class PosterEditForm(forms.ModelForm):
	first = forms.ModelChoiceField(queryset=Poster.objects.all().order_by('first_name'))

	class Meta:
		model = Poster
		fields = ['first']#, 'first_name', 'last_name', 'degree', 'SchoolName',
				#	'DepartmentName', 'Course_name', 'Semester', 'Year',
				#	'FullPosterTitle', 'ThemeKeywordL1', 'ThemeKeywordL2',
				#	'ThemeKeywordL3', 'PlaceKeywordGeonames', 'image',
				#	'ReleaseForm', ]

