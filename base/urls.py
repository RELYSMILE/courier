from django.urls import path
from .views import set_language
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login_page/', views.login_page, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_page/', views.register_page, name='register'),

    path('generate_tracking/', views.generate_tracking, name='generate_tracking'),

    path('set-language/', set_language, name='set_language'),

]
