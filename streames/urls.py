from django.conf.urls import url

from .views import StreamCourseListView

urlpatterns = [
    url(r'^(?P<stream>[\w]+)/$', StreamCourseListView.as_view(), name='list'),
]
