from django.shortcuts import render
from core import models
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.shortcuts import render


# Create your views here.
@login_required
def todo(request):
    if request.method == "POST":
        task = request.POST.get("task")
        c = models.todo(task = task)
        c.save()
        
    mytodo = models.todo.objects.all() # get all the objects/tables from the models.py and store it in a variable
    data = {'todos':mytodo} # storing teh object data in a variable like key:value pair.
    
    return render(request , "todo.html", data) # returning the todo.html content along wfith the data stored into the model.

def deleteTodo(request):
    if request.method == "GET":
        todoid = (request.GET.get("id"))
        models.todo.objects.filter(id=todoid).delete() # delete the id in the models.py based on id.
    
    return todo(request)

def logout_view(request):
    logout(request)
    return todo(request)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)
