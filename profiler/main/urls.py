from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.signout, name="signout"),
    path('settings/', views.settings, name="settings"),
    path('blogs/', views.blogs, name="blogs"),
    path('createapost/', views.createapost, name="createapost"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
]
