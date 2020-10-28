from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('data', views.projectview)
router.register('pbnlist', views.pbnlistview)
router.register('pbntable', views.pbntableview)
router.register('seowebmap', views.webmapview)

urlpatterns = [
    path('', include(router.urls)),
]
