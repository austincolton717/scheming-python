from django.urls import path
from . import views
from rootapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.workManagement, name="workmanagement"),
    path('projects/', views.projects, name="projects"),
    path('upload/', views.upload_project, name="upload-project"),
    path('update/<int:project_id>', views.update_project),
    path('delete/<int:project_id>', views.delete_project),
    path('project-info/<int:project_id', views.project_info),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
