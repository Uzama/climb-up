from django.db import models

from streames.models import Stream

class Subject(models.Model):
	name			= models.CharField(max_length=200)
	level			= models.CharField(max_length=120, default='al', choices=(
			('al','advanced_level'),
			('ol','ordinary_level'),
		))

	def __str__(self):
		return self.name

