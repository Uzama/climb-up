from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from itertools import chain

from .models import Course
from universities.models import University
from streames.models import Stream
from subjects.models import Subject

from .models import Course, Requirement

class SearchCoursesView(ListView):
	def get_queryset(self):
		queryset = Course.objects.filter(course_name='')
		results = self.request.GET
		subject1, result1 = results.get('subject1'), results.get('subject1_result')
		subject2, result2 = results.get('subject2'), results.get('subject2_result')		
		subject3, result3 = results.get('subject3'), results.get('subject3_result')
		maths = results.get('subject4_result')
		english = results.get('subject5_result')
		science = results.get('subject6_result')
		gk	= results.get('gk_result')
		zscore =results.get('zscore')
		district = results.get('district')

		if zscore and district and gk:
			if int(gk) >= 30:
				requirement_match = Requirement.objects.filter(
					Q(district__iexact=district) &
					Q(zscore__lte=zscore)
					).values_list('course')
				courses = []
				for _id in requirement_match:
					courses.append(_id[0])
				course_queryset = Course.objects.filter(id__in=courses)
				queryset1 = course_queryset.filter(
					(Q(subject1__in=Subject.objects.filter(name=subject1)) & Q(result1__gte=result1))& 
					(Q(subject2__in=Subject.objects.filter(name=subject2)) & Q(result2__gte=result2))&  
					(Q(subject3__in=Subject.objects.filter(name=subject3)) & Q(result3__gte=result3))
					).distinct().filter(
					Q(maths__gte=maths)&
					Q(english__gte=english)&
					Q(science__gte=science)
					)
				queryset2 = course_queryset.filter(
					(Q(subject1__in=Subject.objects.filter(name=subject3)) & Q(result1__gte=result3))& 
					(Q(subject2__in=Subject.objects.filter(name=subject1)) & Q(result2__gte=result1))& 
					(Q(subject3__in=Subject.objects.filter(name=subject2)) & Q(result3__gte=result2)) 
					).distinct().filter(
					Q(maths__gte=maths)&
					Q(english__gte=english)&
					Q(science__gte=science)
					)
				queryset3 = course_queryset.filter(
					(Q(subject1__in=Subject.objects.filter(name=subject2)) & Q(result1__gte=result2))& 
					(Q(subject2__in=Subject.objects.filter(name=subject3)) & Q(result2__gte=result3))& 
					(Q(subject3__in=Subject.objects.filter(name=subject1)) & Q(result3__gte=result1)) 
					).distinct().filter(
					Q(maths__gte=maths)&
					Q(english__gte=english)&
					Q(science__gte=science)
					)
				queryset4 = course_queryset.filter(
					(Q(subject1__in=Subject.objects.filter(name=subject1)) & Q(result1__gte=result1))& 
					(Q(subject2__in=Subject.objects.filter(name=subject3)) & Q(result2__gte=result3))& 
					(Q(subject3__in=Subject.objects.filter(name=subject2)) & Q(result3__gte=result2)) 
					).distinct().filter(
					Q(maths__gte=maths)&
					Q(english__gte=english)&
					Q(science__gte=science)
					)
				queryset5 = course_queryset.filter(
					(Q(subject1__in=Subject.objects.filter(name=subject3)) & Q(result1__gte=result3))& 
					(Q(subject2__in=Subject.objects.filter(name=subject2)) & Q(result2__gte=result2))&
					(Q(subject3__in=Subject.objects.filter(name=subject1)) & Q(result3__gte=result1)) 
					).distinct().filter(
					Q(maths__gte=maths)&
					Q(english__gte=english)&
					Q(science__gte=science)
					)
				queryset6 = course_queryset.filter(
					(Q(subject1__in=Subject.objects.filter(name=subject2)) & Q(result1__gte=result2))& 
					(Q(subject2__in=Subject.objects.filter(name=subject1)) & Q(result2__gte=result1))& 
					(Q(subject3__in=Subject.objects.filter(name=subject3)) & Q(result3__gte=result3)) 
					).distinct().filter(
					Q(maths__gte=maths)&
					Q(english__gte=english)&
					Q(science__gte=science)
					)
				queryset = queryset1.union(queryset2, queryset3,queryset4, queryset5,queryset6)
			else: 
				pass
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(SearchCoursesView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		context['ol'] = Subject.objects.filter(level='ol')
		context['al'] = Subject.objects.filter(level='al')
		return context

class CourseListView(ListView):
	template_name = 'courses/course.html'
	def get_context_data(self, *args, **kwargs):
		context = super(CourseListView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		context['ol'] = Subject.objects.filter(level='ol')
		context['al'] = Subject.objects.filter(level='al')
		return context

	def get_queryset(self):
		search_result = self.request.GET.get('search')
		university = self.request.GET.get('university')
		stream = self.request.GET.get('stream')
		if search_result or university or stream:
			if search_result:
				if university and stream:
					queryset = Course.objects.filter(Q(university__name=university)).filter(Q(stream__stream=stream)).filter(
						Q(course_name__iexact=search_result)| 
						Q(course_name__icontains=search_result)
						)
				else:
					queryset = Course.objects.filter(
						Q(course_name__iexact=search_result)| 
						Q(course_name__icontains=search_result)&
						(Q(university__name=university)|
						Q(stream__stream=stream))
						)
			else:
				if university and stream:
					queryset = Course.objects.filter(Q(university__name=university)).filter(Q(stream__stream=stream))
				else:
					queryset = Course.objects.filter(
						Q(university__name=university)|
						Q(stream__stream=stream)
						)
		else:
			queryset = Course.objects.all()
		return queryset







