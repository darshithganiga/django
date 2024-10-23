from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views
from django.shortcuts import render

def Home(request):
     return HttpResponse("welcome to Django foodie Home")
def About(request):
    return HttpResponse("welcome to foodie view")