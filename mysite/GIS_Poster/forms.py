from django import forms
from .models import Poster, Course
from simple_autocomplete.widgets import AutoCompleteWidget
from .fields import ListTextWidget, EmptyChoiceField

SEMESTER_CHOICES = (('Spring', 'Spring'),
                    ('Summer', 'Summer'),
                    ('Fall', 'Fall'))

YEAR_CHOICES = (('2017', '2017'),
                ('2018', '2018'))

RELEASE_CHOICES = [('Yes', 'Yes'),
                    ('No', 'No')]

class PosterCreateForm(forms.ModelForm):
    #char_field_with_list = forms.CharField(required=True)
    class Meta: 
        model = Poster
        fields = ['first_name', 'last_name', 'degree', 'SchoolName',
                    'DepartmentName', 'Course_name', 'Semester', 'Year',
                    'FullPosterTitle', 'ThemeKeywordL1', 'ThemeKeywordL2',
                    'ThemeKeywordL3', 'PlaceKeywordGeonames', 'release_form',
                     'PDFPoster']
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
    #release_form = ListTextWidget(data_list=('Yes', 'No', 'Other'), name='Stuf')
    # ListTextWidget(data_list=('Yes', 'No', 'Other')
    release_form = forms.TypedChoiceField(choices=RELEASE_CHOICES, widget=forms.RadioSelect(), help_text='The student has read and is in agreement with the website release form. If yes, add initials to text box.')
    Course_name = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.RadioSelect(), initial="None", to_field_name='Course_Dept', help_text='Which GIS Course is the student currently enrolled in?')
    Semester = forms.TypedChoiceField(choices=SEMESTER_CHOICES, widget=forms.RadioSelect(), help_text='Which Semester was the student enrolled in GIS?')
    Year = forms.TypedChoiceField(choices=YEAR_CHOICES, widget=forms.RadioSelect(), help_text='What year was the student enrolled in GIS?')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['Course_name', 'Course_code', 'Dept_code']
        help_texts = {
        'Course_name': 'What is the full name of the course? ie. \'GIS 101/ ENV 107/ INTR 81: Introduction to Geographic Information Systems\'',
        'Course_code': 'What is the course code? \n If there are multiple course codes, separate them by an underscore. ie. \'GIS 101_ENV107\'.',
        'Dept_code': 'What is the department code? ie. \'UndergradGIS\''
        }
class PosterSearchForm(forms.Form):
    class Meta:
        fields = ['poster_name']
    # poster_name = forms.CharField(max_length=200)
    # def clean(self):
    #     cleaned_data = super(PosterSearchForm, self).clean()
    #     poster_name = cleaned_data.get("poster_name")
    #     try:
    #         Poster.objects.get(FullPosterTitle=poster_name)
    #     except:
    #         msg = "There is no record by this poster name"
    #         self._errors["poster_name"] = self.error_class([msg])

    #         del cleaned_data["poster_name"]
    #     return cleaned_data

    poster_name = forms.ModelChoiceField(queryset=Poster.objects.all(), widget=forms.RadioSelect(), initial="None")

class PosterEditForm(forms.ModelForm):
    #FullPosterTitle = forms.ModelChoiceField(queryset=Poster.objects.all().order_by('FullPosterTitle'))

    class Meta: 
            model = Poster
            fields = ['first_name', 'last_name', 'degree', 'SchoolName',
                        'DepartmentName', 'Course_name', 'Semester', 'Year',
                        'FullPosterTitle', 'ThemeKeywordL1', 'ThemeKeywordL2',
                        'ThemeKeywordL3', 'PlaceKeywordGeonames', 'release_form',
                         'ThumbnailName', 'ThumbnailPath', 'PosterWinner',
                         'PosterPath', 'reviewed', 'ranking']
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
    #Course_name = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.RadioSelect(), initial="None", to_field_name='Course_Dept', help_text='Which GIS Course is the student currently enrolled in?')
    Semester = forms.TypedChoiceField(choices=SEMESTER_CHOICES, widget=forms.RadioSelect(), help_text='Which Semester was the student enrolled in GIS?')
    Year = forms.TypedChoiceField(choices=YEAR_CHOICES, widget=forms.RadioSelect(), help_text='What year was the student enrolled in GIS?')
