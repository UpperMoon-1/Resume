from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , "resume/home.html")

def skills(request):
    return render(request , "resume/skl.html")

def experience(request):
    return render(request , "resume/exp.html")

def education(request):
    return render(request , "resume/edu.html")