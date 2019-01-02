from django.db import models
from django.db.models.signals import pre_save


from main.utils import unique_slug_generator

class University(models.Model):
	name			= models.CharField(max_length=200)
	moto			= models.TextField()
	website			= models.URLField(max_length=1000)
	facebook		= models.URLField(max_length=1000)
	linkedin		= models.URLField(max_length=1000)
	location		= models.URLField(max_length=1000)
	city			= models.CharField(max_length=120)
	district		= models.CharField(max_length=120)
	discription		= models.TextField()
	timstamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	logo			= models.ImageField(upload_to='logo', max_length=200, blank=True)
	slug			= models.SlugField(unique=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name

def university_pre_save_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(university_pre_save_reciver, sender=University)
	