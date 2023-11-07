from django.shortcuts import render, HttpResponse, redirect
from requests import request
from .models import Task
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    task = Task.objects.all()
    context= {
        'task':task
    }

    if request.method == 'POST':
        Title = request.POST['Title']
        Description = request.POST['Description']
        new_task = Task(Title=Title, Description=Description, Date = datetime.now())
        new_task.save()
        messages.success(request, " New Task Added.")
        return redirect('home')
    elif request.method =='GET':
        return render(request, 'home.html',context)
    else:
        return HttpResponse("Error occured")
    
def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, "Deleted successfully.")
    return redirect('home')


    

