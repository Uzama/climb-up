from django.db import models

class Stream(models.Model):
	stream            = models.CharField(max_length=120, default=None, choices=(
			('bio','biological_science'),
			('maths','physical_science'),
			('commerce','commerce'),
			('arts','arts'),
			('btech','bio_technology'),
			('etech','engineering_technology'),
			('others','others'),
		))

	def __str__(self):
		return self.stream
