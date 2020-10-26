from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexautomation, name="indexautomation"),
]
