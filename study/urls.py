from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^course/', include('courses.urls', namespace='course')),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^stream/', include('streames.urls', namespace='stream')),
    url(r'^subject/', include('subjects.urls', namespace='subject')),
    url(r'^university/', include('universities.urls', namespace='university')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

