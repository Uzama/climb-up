from django.shortcuts import render
from django.views.generic import TemplateView

from universities.models import University
from streames.models import Stream

class HomeView(TemplateView):
	template_name = 'main/home.html'
	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class AboutView(TemplateView):
	template_name = 'main/about.html'
	def get_context_data(self, *args, **kwargs):
		context = super(AboutView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class ContactView(TemplateView):
	template_name = 'main/contact.html'
	def get_context_data(self, *args, **kwargs):
		context = super(ContactView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class FindCourseView(TemplateView):
	template_name = 'main/find_course.html'
	def get_context_data(self, *args, **kwargs):
		context = super(FindCourseView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class SelectStreamView(TemplateView):
	template_name = 'main/select_stream.html'
	def get_context_data(self, *args, **kwargs):
		context = super(SelectStreamView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class UniversityHelpView(TemplateView):
	template_name = 'main/university_help.html'
	def get_context_data(self, *args, **kwargs):
		context = super(UniversityHelpView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class StreamHelpView(TemplateView):
	template_name = 'main/stream_help.html'
	def get_context_data(self, *args, **kwargs):
		context = super(StreamHelpView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class CourseHelpView(TemplateView):
	template_name = 'main/course_help.html'
	def get_context_data(self, *args, **kwargs):
		context = super(CourseHelpView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class ResourceView(TemplateView):
	template_name = 'main/resources.html'
	def get_context_data(self, *args, **kwargs):
		context = super(ResourceView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context

class SearchResultView(TemplateView):
	template_name = 'main/search_result.html'
	def get_context_data(self, *args, **kwargs):
		context = super(SearchResultView, self).get_context_data(*args, **kwargs)
		context['university'] = University.objects.all()
		context['stream'] = Stream.objects.all()
		return context
