from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPoint, name='StartingPoint'),
    path('team/', views.TeamMem, name='TeamMem'),
    path('tasks/', views.TaskTable, name='TaskTable'),
    path('search/', views.SearchTitle, name='SearchTitle'),
    path('addtask/', views.AddTask, name='AddTask'),
]