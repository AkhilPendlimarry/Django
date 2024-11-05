from django.shortcuts import render
from core import models

# Create your views here.

def todo(request):
    if request.method == "POST":
        task = request.POST.get("task")
        c = models.todo(task = task)
        c.save()
        
    mytodo = models.todo.objects.all()
    data = {'todos':mytodo}

    return render(request , "todo.html", data)

def deleteTodo(request):
    if request.method == "GET":
        todoid = int(request.GET.get("id"))
        models.todo.objects.filter(id=todoid).delete()
    
    return todo(request)