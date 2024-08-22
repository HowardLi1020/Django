from django.shortcuts import render, redirect
from django.db import connection
from .models import toDoList
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime, timedelta
# Create your views here.
def index(request):
    thingsToDo = toDoList.objects.all()
    if request.method =='POST':
        things = request.POST.get('someThing')
        toDoList.objects.create(
            todo = things
        ) 
        return redirect('todo_list:index')
    return render(request,'todo_list/index.html', {'lists':thingsToDo})

def delete(request, id):   
    things = toDoList.objects.get(todo_id=id)  
    things.delete()

    return redirect('todo_list:index')

def complete(request, id):
    task = toDoList.objects.get(todo_id=id)
    completed = request.POST.get('completed') == 'true'
    task.completed = completed  # Update the task's completed status
    task.save()
    return redirect('todo_list:index')



