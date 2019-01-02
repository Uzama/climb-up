from django.conf.urls import url

from .views import (
	HomeView,
	FindCourseView,
	SelectStreamView,
	UniversityHelpView,
	StreamHelpView,
	CourseHelpView,
	ResourceView,
	SearchResultView,
	AboutView,
	ContactView
	)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^find-course/$', FindCourseView.as_view(), name='find-course'),
    url(r'^select-stream/$', SelectStreamView.as_view(), name='select-stream'),
    url(r'^university-help/$', UniversityHelpView.as_view(), name='university-help'),
    url(r'^stream-help/$', StreamHelpView.as_view(), name='stream-help'),
    url(r'^course-help/$', CourseHelpView.as_view(), name='course-help'),
    url(r'^resource/$', ResourceView.as_view(), name='resource'),
    url(r'^search-result/$', SearchResultView.as_view(), name='search-result'),
]
