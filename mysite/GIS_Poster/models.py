from django.db import models
from multiselectfield import MultiSelectField

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
				  ('UEP', 'Urban and Environmental Policy and Planning (UEP'),
				  ('Other', 'Other'))

# Create your models here.
class Poster(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	StudentName = models.CharField(max_length = 200)
	degree = MultiSelectField(choices=DEGREE_CHOICES)
	SchoolName = MultiSelectField(choices=SCHOOL_CHOICES)
	DepartmentName = MultiSelectField(choices=DEPARTMENT_CHOICES, max_choices=1)


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