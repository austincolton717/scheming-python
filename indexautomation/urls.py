from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexautomation, name="indexautomation"),
    path('data-automation/', views.data_automation, name="data-automation"),
    path('indexchecker/', views.indexChecker, name="indexchecker"),
]
