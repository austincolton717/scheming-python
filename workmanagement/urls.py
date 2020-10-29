from django.urls import path
from . import views

urlpatterns = [
    path('', views.workManagement, name="workmanagement"),
    path('projects/', views.projects, name="projects"),
]
