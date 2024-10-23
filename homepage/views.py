from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .import views
# from .models import Foodie

Foodie= [{"name":"Food1","Desc":"Ready to eat food"},{"name":"Food2","Desc":"Ready to eat food"},{"name":"Food3","Desc":"Ready to eat food"},{"name":"Food4","Desc":"Ready to eat food"}]

def Home(request):
    # Foodiees = Foodie.objects.all()
    context={'Foodie':Foodie}
    return render(request,"Home.html",context)
def About(request):
      return render(request,"About.html")

# Create your views here.
