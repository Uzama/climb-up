from django.contrib import admin

# Register your models here.
from .models import Course, Requirement

admin.site.register(Course)
admin.site.register(Requirement)