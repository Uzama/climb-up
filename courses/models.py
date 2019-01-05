from django.db import models
from django.db.models.signals import pre_save

from universities.models import University
from streames.models import Stream
from subjects.models import Subject

from main.utils import unique_slug_generator

RESULTS = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('S', 'S'),
	('W', 'W'),
	)

class Course(models.Model):
	course_name				= models.CharField(max_length=200)
	slug					= models.SlugField(blank=True)
	student_count			= models.PositiveIntegerField()
	university				= models.ForeignKey(University)
	degree_name				= models.CharField(max_length=200)
	apitude_exam			= models.BooleanField(default=False)
	language				= models.CharField(max_length=50, default=None, choices=(
			('english','English'),
			('tamil','Tamil'),
			('sinhale','Sinhale'),
		))
	period					= models.PositiveIntegerField(default=4, choices=(
			(1,1),
			(2,2),
			(3,3),
			(4,4),
			(5,5),
		))
	stream					= models.ForeignKey(Stream)
	subject1				= models.ManyToManyField(Subject, default=None, related_name='subject1', limit_choices_to={'level':'al'})
	result1					= models.CharField(max_length=2, default='S', choices=RESULTS)
	subject2				= models.ManyToManyField(Subject, default=None, related_name='subject2', limit_choices_to={'level':'al'})
	result2				    = models.CharField(max_length=2, default='S', choices=RESULTS)
	subject3				= models.ManyToManyField(Subject, default=None, related_name='subject3', limit_choices_to={'level':'al'})	
	result3					= models.CharField(max_length=2, default='S', choices=RESULTS)
	maths					= models.CharField(max_length=2, blank=True, default='W', choices=RESULTS)
	english					= models.CharField(max_length=2, blank=True, default='W', choices=RESULTS)
	science					= models.CharField(max_length=2, blank=True, default='W', choices=RESULTS)
	discription				= models.TextField()

	def __str__(self):
		return self.course_name + ' - ' + self.university.name

	@property
	def title(self):
		return self.course_name

class Requirement(models.Model):
	course 					= models.ForeignKey(Course)
	district				= models.CharField(max_length=200, blank=True)
	zscore					= models.DecimalField(max_digits=5, default=0, decimal_places=4, blank=True)

	def __str__(self):
		return self.course.__str__() + ' - ' + self.district

def university_pre_save_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(university_pre_save_reciver, sender=Course)



