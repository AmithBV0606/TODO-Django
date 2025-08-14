from .models import Task
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    # return HttpResponse('The form is submitted!!')
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_tash(request, pk):
    return render(request, 'edit_task.html')