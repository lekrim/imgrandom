from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_imgset, name='create_imgset'),
    path('save_img/<str:img_name>', views.save_img, name='save_img'),
    path('delete_img/<str:img_name>', views.delete_img, name='delete_img'),
    path('album', views.show_album, name='show_album'),
]