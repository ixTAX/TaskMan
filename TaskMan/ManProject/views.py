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

def AddTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            return redirect('task', bId = obj.id )
    form = TaskForm(None)
    return render(request, 'ManProject/addtask.html',{'form':form})
  
def updatetask(request, bId):
    obj = Task.objects.get(id = bId)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('task', bId = obj.id )
    form = TaskForm(instance=obj)
    return render(request, 'ManProject/updatetask.html',{'form':form})


def all_user(request):
  return HttpResponse('Returning all user')

def Tasks(request):
    tasks = Task.objects.all()
    return render(request, 'ManProject/tasklist.html', {'tasks': tasks})
  
def Tasksu(request):
    tasks = Task.objects.all()
    return render(request, 'ManProject/tasklistupdate.html', {'tasks': tasks})
  
def task(request, bId):
    obj = Task.objects.get(id = bId)
    if request.method == 'POST':
      Task.objects.get(id = bId).delete()
      return redirect('/tasklist')
    return render(request, 'ManProject/task.html', {'task':obj})