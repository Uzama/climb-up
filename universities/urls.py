from django.conf.urls import url

from .views import UniversityListView, UniversityDetailView

urlpatterns = [
    url(r'^$', UniversityListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', UniversityDetailView.as_view(), name='detail'),
]
