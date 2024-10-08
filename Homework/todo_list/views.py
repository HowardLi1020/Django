from django.shortcuts import render, redirect
from .models import toDoList
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

def task_complete(request, id):
    if request.method == 'POST':
        task = toDoList.objects.get(todo_id=id)
        completed_value = request.POST.get('completed') == 'true'
        task.completed = completed_value
        task.save()
    return redirect('todo_list:index')





