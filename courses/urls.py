from django.conf.urls import url

from .views import SearchCoursesView, CourseListView

urlpatterns = [
	url(r'^$', CourseListView.as_view(), name='list'),
    url(r'^find/$', SearchCoursesView.as_view(), name='find'),
]
