from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from courses.models import Course
from .models import Stream
from universities.models import University

class StreamCourseListView(ListView):
	template_name = 'streames/stream_course_list.html'
	def get_queryset(self):
		# queryset = super(StreamCourseListView, self).get_queryset()
		stream = self.kwargs.get('stream')
		search_result = self.request.GET.get('search')
		stream = Stream.objects.get(stream=stream)
		if stream:
			queryset = stream.course_set.all()
			if search_result is not None:
				queryset = queryset.filter(
					Q(course_name__iexact=search_result)|
					Q(course_name__icontains=search_result)|
					Q(university__name__iexact=search_result)|
					Q(university__name__icontains=search_result) 
				)
		else:
			queryset = Course.objects.all()
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(StreamCourseListView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream_name'] = self.kwargs.get('stream').capitalize()
		context['stream'] = Stream.objects.all()
		return context