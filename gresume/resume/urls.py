'''
Created on Jan 5, 2025

@author: Giuseppe
'''
from django.urls import path
from . import views


urlpatterns = [
        path("" , views.index , name="index"),
        path("skills" , views.skills , name="skills"),
        path("education" , views.education , name="education"),
        path("experience" , views.experience , name="experience")
    ]
