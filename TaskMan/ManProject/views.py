from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def StartingPoint(request):
  
  return render(request, 'ManProject/myfirst.html')

def TeamMem(request):
  
  return render(request, 'ManProject/team.html')

def TaskTable(request):
  
  return render(request, 'ManProject/tasks.html')

def SearchTitle(request):
  
  return render(request, 'ManProject/search.html')

def AddTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            obj = form.save()

    form = TaskForm(None)
    return render(request, 'ManProject/addtask.html',{'form':form})


def all_user(request):
  return HttpResponse('Returning all user')
