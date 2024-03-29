from django.utils.text import slugify

import random
import string

DONT_USE = []


def random_string_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)
	Klass = instance.__class__
	slug_exists = Klass.objects.filter(slug=slug).exists()
	if slug_exists or (slug in DONT_USE):
		slug = f"{slug}-{random_string_generator(size=4)}"
		return unique_slug_generator(instance, new_slug=slug)
	return slug
