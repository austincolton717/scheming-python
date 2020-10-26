from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('data', views.projectview)
router.register('pbnlist', views.pbnlistview)


urlpatterns = [
    path('', include(router.urls)),
]
