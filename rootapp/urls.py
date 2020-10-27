from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('api/', include('api.urls')),
    path('apirequest/', include('apirequest.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('seodatatools/', include('seodatatools.urls')),
    path('indexautomation/', include('indexautomation.urls')),
    path('pbn/', include('pbn.urls')),
    path('workmanagement/', include('workmanagement.urls')),
    path('clientmanager/', include('clientmanager.urls')),
    path('archive/', include('archive.urls')),
    path('livepreview/', include('livepreview.urls')),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                             content_type="text/plain"),
    ),
]
