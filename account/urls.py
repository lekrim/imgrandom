from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit/', views.edit_account, name='edit'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), 
                                               name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), 
                                               name='logout'),
]