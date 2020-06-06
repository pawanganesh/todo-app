from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib import messages
from .models import task

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been added!'))
            return redirect('home')
    else:
        all_task = task.objects.all()
        context = {'tasks': all_task}
        return render(request, 'home.html',context)

def edit_task(request, id):
    if request.method == 'POST':
        item = task.objects.get(pk = id)
        form = TaskForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            messages.success(request,('Task edited successfully!'))
            return redirect('home')
    else:
        item = task.objects.get(pk = id)
        context = {'item': item}
        return render(request, 'edit.html', context)

def delete_task(request, id):
    d_task = task.objects.get(pk = id)
    d_task.delete()
    messages.success(request, ('Task has been deleted!'))
    return redirect('home')

def cross_off(request, id):
    c_task = task.objects.get(pk = id)
    c_task.completed = True
    c_task.save()
    return redirect('home')

def uncross(request, id):
    c_task = task.objects.get(pk = id)
    c_task.completed = False
    c_task.save()
    return redirect('home')

