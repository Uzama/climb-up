from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from universities.models import University
from streames.models import Stream
from .models import Subject
from courses.models import Course

class SelectStreamView(ListView):
	template_name = 'subjects/select_stream.html'
	def get_context_data(self, *args, **kwargs):
		context = super(SelectStreamView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		context['al'] = Subject.objects.filter(level='al')
		return context

	def get_queryset(self):
		queryset = Course.objects.filter(course_name='')
		results = self.request.GET
		subject1 = results.get('subject1')
		subject2 = results.get('subject2')		
		subject3 = results.get('subject3')
		search_result = results.get('search')
		university = results.get('university')
		stream = results.get('stream')

		if subject1 and subject2 and subject3:
			course_queryset = Course.objects.all()
			queryset1 = course_queryset.filter(
				(Q(subject1__in=Subject.objects.filter(name=subject1)))& 
				(Q(subject2__in=Subject.objects.filter(name=subject2)))& 
				(Q(subject3__in=Subject.objects.filter(name=subject3)))
				).distinct()
			queryset2 = course_queryset.filter(
				(Q(subject1__in=Subject.objects.filter(name=subject3)))&
				(Q(subject2__in=Subject.objects.filter(name=subject1)))& 
				(Q(subject3__in=Subject.objects.filter(name=subject2))) 
				).distinct()
			queryset3 = course_queryset.filter(
				(Q(subject1__in=Subject.objects.filter(name=subject2)))& 
				(Q(subject2__in=Subject.objects.filter(name=subject3)))& 
				(Q(subject3__in=Subject.objects.filter(name=subject1)))
				).distinct()
			queryset4 = course_queryset.filter(
				(Q(subject1__in=Subject.objects.filter(name=subject1)))& 
				(Q(subject2__in=Subject.objects.filter(name=subject3)))&
				(Q(subject3__in=Subject.objects.filter(name=subject2)))
				).distinct()
			queryset5 = course_queryset.filter(
				(Q(subject1__in=Subject.objects.filter(name=subject3)))&
				(Q(subject2__in=Subject.objects.filter(name=subject2)))& 
				(Q(subject3__in=Subject.objects.filter(name=subject1)))
				).distinct()
			queryset6 = course_queryset.filter(
				(Q(subject1__in=Subject.objects.filter(name=subject2)))& 
				(Q(subject2__in=Subject.objects.filter(name=subject1)))&
				(Q(subject3__in=Subject.objects.filter(name=subject3)))
				).distinct()
			queryset = queryset1.union(queryset2, queryset3,queryset4, queryset5,queryset6) 
		if search_result or university or stream:
			if search_result:
				if university and stream:
					queryset = queryset.filter(Q(university__name=university)).filter(Q(stream__stream=stream)).filter(
						Q(course_name__iexact=search_result)| 
						Q(course_name__icontains=search_result)
						)
				else:
					queryset = queryset.filter(
						Q(course_name__iexact=search_result)| 
						Q(course_name__icontains=search_result)|
						Q(university__name=university)|
						Q(stream__stream=stream)
						)
			else:
				if university and stream:
					queryset = queryset.filter(Q(university__name=university)).filter(Q(stream__stream=stream))
				else:
					queryset = queryset.filter(
						Q(university__name=university)|
						Q(stream__stream=stream)
						)
		return queryset