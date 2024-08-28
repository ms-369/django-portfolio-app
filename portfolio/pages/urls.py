from django.contrib import admin
from django.urls import path
from .views import homepage,detailView,projectList,start

urlpatterns = [
    path('', start, name="start"),
    path('homepage/', homepage, name="homepage"),
    path('detailView/<str:key>', detailView, name="detailView"),
    path('projectList/', projectList, name="projectList"),


]