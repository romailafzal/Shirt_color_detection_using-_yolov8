from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns = [
    path('real_time_detection/', views.real_time_detection, name='real_time_detection'),
    path('camera_feed/', views.camera_feed, name='camera_feed'),path('', views.home, name='home'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('camera_stream/', views.camera_stream, name='camera_stream'),
    path('upload_captured/', views.upload_captured_image, name='upload_captured_image'),
    path('detected_image/', views.detected_image, name='detected_image'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)