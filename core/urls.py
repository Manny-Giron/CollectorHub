from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]

