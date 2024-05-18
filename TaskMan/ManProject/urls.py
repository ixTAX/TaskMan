from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.StartingPoint, name='StartingPoint'),
    path('team/', views.TeamMem, name='TeamMem'),
    path('tasklist/', views.Tasks, name='Tasks'),
    path('tasklistupdate/', views.Tasksu, name='Tasksu'),
    path('task/<int:bId>', views.task, name="task"),
    path('addtask/', views.AddTask, name='AddTask'),
    path('updatetask/<int:bId>', views.updatetask, name="updatetask"),
    path('users/', views.all_user),
]