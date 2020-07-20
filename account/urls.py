from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views
# from .views import PasswordResetView
urlpatterns=[

    
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name= "password_reset_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name= "password_reset"),

    

]
