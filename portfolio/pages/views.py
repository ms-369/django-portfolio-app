from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import project

# Create your views here.

def start(request):
    return redirect('homepage')

def homepage(request):
    allProjects = project.objects.all()
    print(allProjects)
    data = {
        'projects' : allProjects
    }
    return render(request,"homepage.html",data)



def detailView(request, key):
    Project = project.objects.get(id=key)
    data = {
        'project' : Project
    }
    return render(request,"detail.html",data)

def projectList(request):
    allProjects = project.objects.all()
    print(allProjects)
    data = {
        'projects' : allProjects
    }
    return render(request,"projectList.html",data)