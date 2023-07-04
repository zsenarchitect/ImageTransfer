from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload, name='image_upload'),
    path('upload/', views.image_upload, name='image_upload'),
    path('view/', views.image_view, name='image_view'),
    path('all/', views.all_images, name='all_images'),
    path('api/images/', views.get_all_images_json, name='api-images'),
]


