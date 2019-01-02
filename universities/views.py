from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import University
from streames.models import Stream
from courses.models import Course

class UniversityListView(ListView):
	def get_context_data(self, *args, **kwargs):
		context = super(UniversityListView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

	def get_queryset(self):
		search_result = self.request.GET.get('search')
		if search_result:
			queryset = University.objects.filter(
				Q(name__iexact=search_result) |
				Q(district__iexact=search_result) |
				Q(name__icontains=search_result) |
				Q(district__icontains=search_result)
				).order_by('name')
		else:
			queryset = University.objects.all().order_by('name')
		return queryset

class UniversityDetailView(DetailView):
	queryset = University.objects.all()
	def get_context_data(self, *args, **kwargs):
		context = super(UniversityDetailView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		search_result = self.request.GET.get('search')
		slug = self.kwargs.get('slug')
		university = University.objects.get(slug=slug)
		if search_result:
			course = university.course_set.all().filter(
				Q(course_name__iexact=search_result) |
				Q(course_name__icontains=search_result)
				).order_by('course_name')
		else:
			course = university.course_set.all().order_by('course_name')
		context['course'] = course
		return context







