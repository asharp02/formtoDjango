from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

DEGREE_CHOICES = (('Bachelors', 'Bachelors'),
				  ('Masters', 'Masters'),
				  ('PhD', 'PhD'),
				  ('Faculty/Staff', 'Faculty/Staff'),
				  ('Certificate', 'Certificate'))

SCHOOL_CHOICES = (('SAS', 'School of Arts and Sciences'),
				  ('SE', 'School of Engineering'),
				  ('Fletcher', 'The Fletcher School of Law and Diplomacy'),
				  ('Friedman', 'Gerald J. and Dorothy R. Friedman School of Nutrition Science and Policy'),
				  ('Cummings', 'Cummings School of Veterinary Medicine'),
				  ('Med', 'School of Medicine'),
				  ('Dental', 'School of Dental Medicine'),
				  ('Feinstein', 'Feinstein International Center'),
				  ('PubSafety', 'Public Safety'),
				  ('TIE', 'Tufts Institute for the Environment'),
				  ('Other', 'Other'))

DEPARTMENT_CHOICES = (('AMER', 'American Studies'),
				  ('ANTH', 'Anthropology'),
				  ('ARC', 'Archaeology'),
				  ('ARCH', 'Architectural Studies'),
				  ('BIO', 'Biology'),
				  ('BIOPSYCH', 'Biopsychology'),
				  ('CD', 'Child Study and Human Development'),
				  ('CHN', 'Chinese'),
				  ('CEE', 'Civil and Environmental Engineering'),
				  ('CLA', 'Classics'),
				  ('CH', 'Community Health'),
				  ('CS', 'Computer Science'),
				  ('CONS', 'Conservation Medicine'),
				  ('EOS', 'Earth and Ocean Studies'),
				  ('ECON', 'Economics'),
				  ('ENG_PHYS', 'Engineering Physics'),
				  ('ENG_SCI', 'Engineering Science'),
				  ('ENG', 'English'),
				  ('ELS', 'Entrepreneurial Leadership'),
				  ('FR', 'French'),
				  ('HIS', 'History'),
				  ('IR', 'International Relations'),
				  ('MATH', 'Mathematics'),
				  ('ME', 'Mechanical Engineering'),
				  ('MUS', 'Music'),
				  ('PJS', 'Peace and Justice Studies'),
				  ('PHIL', 'Philosophy'),
				  ('PHY', 'Physics'),
				  ('PS', 'Political Science'),
				  ('PSY', 'Psychology'),
				  ('PH', 'Public Health'),
				  ('REE', 'Russian and Eastern European Studies'),
				  ('SOC', 'Sociology'),
				  ('SPN', 'Spanish'),
				  ('STATS', 'Statistics'),
				  ('TTS', 'Tufts Technology Services'),
				  ('UEP', 'Urban and Environmental Policy and Planning (UEP)'),
				  ('Other', 'Other'))

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


TOPIC_CHOICES = (('AWB', 'Animal, Wildlife and Biota'),
				  ('AEC', 'Architecture, Engineering and Construction'),
				  ('BC', 'Business and Commercial'),
				  ('CD', 'Community Development'),
				  ('DI', 'Defense and Intelligence'),
				  ('EDU', 'Education'),
				  ('EC', 'Energy and Climate'),
				  ('ER', 'Exposure and Risk'),
				  ('FAC', 'Facilities'),
				  ('FD', 'Finance and Development'),
				  ('GOV', 'Government'),
				  ('HLT', 'Health'),
				  ('HUM', 'Humanities'),
				  ('HA', 'Humanitarian Assistance'),
				  ('INF', 'Infrastructure'),
				  ('NR', 'Natural Resources'),
				  ('NUTR', 'Nutrition'),
				  ('PS', 'Public Safety'),
				  ('REC', 'Recreation'),
				  ('TRS', 'Transportation'),
				  ('WAT', 'Water'))


SUBTOPIC_CHOICES = (('AWB', 'Animal, Wildlife and Biota'),
				  ('AEC', 'Architecture, Engineering and Construction'),
				  ('BC', 'Business and Commercial'),
				  ('CD', 'Community Development'),
				  ('DI', 'Defense and Intelligence'),
				  ('EDU', 'Education'),
				  ('EC', 'Energy and Climate'),
				  ('ER', 'Exposure and Risk'),
				  ('FAC', 'Facilities'),
				  ('FD', 'Finance and Development'),
				  ('GOV', 'Government'),
				  ('HLT', 'Health'),
				  ('HUM', 'Humanities'),
				  ('HA', 'Humanitarian Assistance'),
				  ('INF', 'Infrastructure'),
				  ('NR', 'Natural Resources'),
				  ('NUTR', 'Nutrition'),
				  ('PS', 'Public Safety'),
				  ('REC', 'Recreation'),
				  ('TRS', 'Transportation'),
				  ('WAT', 'Water'))

SUBTOPIC_CHOICES = (
				("Air and Atmosphere", "Air and Atmosphere"),
				("Accessibility", "Accessibility"),
				('Agriculture', 'Agriculture'),
				('Alternative and Renewable Energy', 'Alternative and Renewable Energy'),
				('Animal Health', 'Animal Health'),
				('Archeology', 'Archeology'),
				('Aviation', 'Aviation'),
				('Banking and Financial Services', 'Banking and Financial Services'),
				('Building and Landscape Architecture', 'Building and Landscape Architecture'),
				('Census', 'Census'),
				('City Management', 'City Management'),
				('Climate and Weather', 'Climate and Weather'),
				('Climate Change', 'Climate Change'),
				('Community Advocacy', 'Community Advocacy'),
				('Community Analysis', 'Community Analysis'),
				('Community Maps', 'Community Maps'),
				('Conflict', 'Conflict'),
				('Conservation', 'Conservation'),
				('Construction', 'Construction'),
				('Contamination', 'Contamination'),
				('Criminal Justice', 'Criminal Justice'),
				('Cultural Resource Management', 'Cultural Resource Management'),
				('Disease', 'Disease'),
				('Ecology', 'Ecology'),
				('Economic Development', 'Economic Development'),
				('Elections', 'Elections'),
				('Electric Utilities', 'Electric Utilities'),
				('EMS and Emergency Calls', 'EMS and Emergency Calls'),
				('Emergency Management', 'Emergency Management'),
				('Energy', 'Energy'),
				('Energy Planning', 'Energy Planning'),
				('Engineering and Design', 'Engineering and Design'),
				('Environmental Justice', 'Environmental Justice'),
				('Environmental Management', 'Environmental Management'),
				('Federal Agencies', 'Federal Agencies'),
				('Fire Management', 'Fire Management'),
				('Fire Rescue', 'Fire Rescue'),
				('Fisheries', 'Fisheries'),
				('Flood Management', 'Flood Management'),
				('Food Access', 'Food Access'),
				('Food Deserts', 'Food Deserts'),
				('Food Insecurity', 'Food Insecurity'),
				('Food Production', 'Food Production'),
				('Forestry', 'Forestry'),
				('Gentrification', 'Gentrification'),
				('Geosciences', 'Geosciences'),
				('Groundwater', 'Groundwater'),
				('Hazard management', 'Hazard management'),
				('Health Systems', 'Health Systems'),
				('Highways and Roads', 'Highways and Roads'),
				('History', 'History'),
				('Homeland Security', 'Homeland Security'),
				('Hospitals', 'Hospitals'),
				('Housing', 'Housing'),
				('Human Security', 'Human Security'),
				('Human Services', 'Human Services'),
				('Humanitarian Aid and Relief', 'Humanitarian Aid and Relief'),
				('Hydraulic Engineering', 'Hydraulic Engineering'),
				('Intelligence', 'Intelligence'),
				('International Development', 'International Development'),
				('Land Administration', 'Land Administration'),
				('Law Enforcement', 'Law Enforcement'),
				('Local Government', 'Local Government'),
				('Location Based Services', 'Location Based Services'),
				('Manufacturing', 'Manufacturing'),
				('Medicine', 'Medicine'),
				('Military Operations', 'Military Operations'),
				('Mining', 'Mining'),
				('National Security', 'National Security'),
				('Natural Disasters', 'Natural Disasters'),
				('Oceans and Maritime', 'Oceans and Maritime'),
				('Operations and Maintenance', 'Operations and Maintenance'),
				('Parks and Natural Resources', 'Parks and Natural Resources'),
				('Petroleum and Fossil Fuels', 'Petroleum and Fossil Fuels'),
				('Physical Activity', 'Physical Activity'),
				('Pipeline and Gas Utilities', 'Pipeline and Gas Utilities'),
				('Policy', 'Policy'),
				('Pollution', 'Pollution'),
				('Poverty Mapping', 'Poverty Mapping'),
				('Public Health', 'Public Health'),
				('Public Transit', 'Public Transit'),
				('Public Works', 'Public Works'),
				('Railways', 'Railways'),
				('Real Estate', 'Real Estate'),
				('Redistricting', 'Redistricting'),
				('Regional Planning', 'Regional Planning'),
				('Retail', 'Retail'),
				('Risk Assessment', 'Risk Assessment'),
				('Safety and Security', 'Safety and Security'),
				('Schools', 'Schools'),
				('Sea Level Rise', 'Sea Level Rise'),
				('Social Inequality', 'Social Inequality'),
				('State Government', 'State Government'),
				('Storm Water', 'Storm Water'),
				('Subsidized Housing', 'Subsidized Housing'),
				('Surveying', 'Surveying'),
				('Sustainability', 'Sustainability'),
				('Telecommunications', 'Telecommunications'),
				('Universities and Colleges', 'Universities and Colleges'),
				('Urban Planning', 'Urban Planning'),
				('Urbanization', 'Urbanization'),
				('Wastewater', 'Wastewater'),
				('Water Management', 'Water Management'),
				('Water Quality', 'Water Quality'),
				('Water Quantity', 'Water Quantity'),
				('Water Resources', 'Water Resources'),
				('Wildlife Management', 'Wildlife Management'))

METHOD_CHOICES = (
				('Best Path - Least Cost', 'Best Path - Least Cost'),                
				('Change Detection','Change Detection'),                   
				('Hydro Analysis', 'Hydro Analysis'),                   
				('Needs Analysis', 'Needs Analysis'),                      
				('Network Analysis', 'Network Analysis'),                     
				('Proximity Analysis', 'Proximity Analysis'),                      
				('Remote Sensing', 'Remote Sensing'),                              
				('Statistics/Spatial Statistics','Statistics/Spatial Statistics'),                    
				('Suitability Analysis', 'Suitability Analysis'),
				('Thematic Mapping','Thematic Mapping'),
				('Vulnerability Analysis', 'Vulnerability Analysis'))                                              
RELEASE_CHOICES = [('Yes', 'Yes'),
					('No', 'No')]

# Create your models here.

class Course(models.Model):
	Course_code = models.CharField(max_length=200, unique=True)
	Course_name = models.CharField(max_length=200, unique=True)
	Dept_code = models.CharField(max_length=200) #should have choices with ability to add new

	def __str__(self):
		# template = '{0.Course_code} {0.Course_name} {0.Dept_code}'
		# return template.format(self)
		return (self.Course_name)
class Poster(models.Model):


	first_name = models.CharField(max_length = 200, verbose_name='Student\'s First Name')
	last_name = models.CharField(max_length = 200, verbose_name='Student\'s Last Name')
	StudentName = models.CharField(max_length = 200, default=first_name)
	degree = MultiSelectField(choices=DEGREE_CHOICES, verbose_name='Student\'s Degree')
	SchoolName = MultiSelectField(choices=SCHOOL_CHOICES, verbose_name='School Name?')
	DepartmentName = MultiSelectField(choices=DEPARTMENT_CHOICES, max_choices=1, verbose_name='Student\'s Department(s)')
	#cc = Course.objects.values('Course_code')
	
	Course_name = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='GIS Course', default=Course.objects.all()[0])#models.CharField(max_length=200, verbose_name='GIS Course')
	#Course_code = Course.objects.filter(Course_name)
	#cc = Course.values('Course_code')
	#cc = Course.values('CN', 'CC', 'DC')
	Dept_code = models.CharField(max_length=200)#, choices=PosterMetaData dept choices)
	Course_code = models.CharField(max_length=200)#, choices=PosterMetaData dept choices)

	Semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES, verbose_name='Semester')
	Year = models.CharField(max_length=20, choices=YEAR_CHOICES)
	FullPosterTitle = models.CharField(max_length=200, verbose_name='Title of GIS Poster')
	ThemeKeywordL1 = MultiSelectField(choices=TOPIC_CHOICES, verbose_name='Topic Keyword')
	ThemeKeywordL2 = MultiSelectField(choices=SUBTOPIC_CHOICES, verbose_name='Sub-Topic Keyword')
	ThemeKeywordL3 = MultiSelectField(choices=METHOD_CHOICES, verbose_name='Methodological Keyword')
	PlaceKeywordGeonames = models.CharField(max_length=200, verbose_name='Place Keywords - Where is your GIS Project located') #dont know if this should be an integerfield or charfield for multiple geonames
	SDrivePathway = models.CharField(max_length=200, default="pass")
	PDFPoster = models.FileField(verbose_name='PDF of Poster', upload_to='images')#'S:/Posters/GIS Posters/')
	#release_form = models.BooleanField(verbose_name='Website Release Form')
	ThumbnailName = models.CharField(max_length=200, default='pass')
	ThumbnailPath = models.CharField(max_length=200, default='pass')
	PosterPath = models.CharField(max_length=200, default='pass')
	PosterWinner = models.BooleanField(verbose_name='Poster Winner', default='False')
	release_form = models.CharField(max_length=15, default='')

	reviewed = models.BooleanField(default='False')
	ranking = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]) #REMOVE DEFAULT




	#Website release form, boolean field but if yes allow them to sign initials
	def __str__(self):
		return self.StudentName



# class Image(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              related_name='images_created')
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, blank=True)
#     url = models.URLField()
#     image = models.ImageField(upload_to='images/%Y/%m/%d')
#     description = models.TextField(blank=True)
#     created = models.DateTimeField(auto_now_add=True,
#                                    db_index=True)
#     users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
#                                         related_name='images_liked',
#                                         blank=True)

#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Image, self).save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('images:detail', args=[self.id, self.slug])