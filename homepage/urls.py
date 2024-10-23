from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views

# def Home(request):
#     return HttpResponse("welcome to Django home page ")

urlpatterns = [
    path('About/',views.About,name="About"),
    path('Home/',views.Home,name="Home"),
]