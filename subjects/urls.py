from django.conf.urls import url

from .views import SelectStreamView

urlpatterns = [
    url(r'^select-stream/$', SelectStreamView.as_view(), name='select-stream'),
    
]
