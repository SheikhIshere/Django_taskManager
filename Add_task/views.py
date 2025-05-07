from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def homepage(request):  # Renamed from show_tasks
    tasks = Task.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')  # Redirect to homepage
    else:
        task_form = TaskForm()
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    print(task.title)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskForm(instance=task)
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('homepage')
    return render(request, 'delete_confirm.html', {'task': task})

# views.py - Update the complete_task function
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        # Get the status from the form submission
        is_completed = request.POST.get('is_completed') == 'True'
        task.is_completed = is_completed
        task.save()
    
    return redirect('homepage')

def task_details(request, task_id):        
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_details.html', {'task': task})