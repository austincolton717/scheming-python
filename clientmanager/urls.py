from django.urls import path
from . import views
from rootapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.clientManager, name="clientmanager"),
    path('upload-client/', views.upload_client, name="upload-client"),
    path('update/<int:project_id>', views.update_client),
    path('delete/<int:project_id', views.delete_client),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
