from django.shortcuts import render

def StartingPoint(request):
  
  return render(request, 'ManProject/myfirst.html')

def TeamMem(request):
  
  return render(request, 'ManProject/team.html')

def TaskTable(request):
  
  return render(request, 'ManProject/tasks.html')

def SearchTitle(request):
  
  return render(request, 'ManProject/search.html')

def AddTask(request):
  
  return render(request, 'ManProject/addtask.html')