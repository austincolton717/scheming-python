from django.urls import path
from . import views
from rootapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pbnlist, name="pbnlist"),
    path('upload/', views.upload_pbn, name='upload-pbn'),
    path('update/<int:pbn_id>', views.update_pbn),
    path('delete/<int:pbn_id>', views.delete_pbn),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
