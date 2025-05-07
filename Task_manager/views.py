from django.shortcuts import render
from Add_task.models import Task  # or wherever your Task model is

# def home(request):
#     tasks = Task.objects.all()  # Get all tasks
#     return render(request, 'home.html', {'tasks': tasks})


def home(request):
    tasks = Task.objects.all()
    
    # Check if all tasks are completed
    all_tasks_completed = tasks.exists() and all(task.is_completed for task in tasks)
    
    # Check if none of the tasks are completed (all are False)
    none_completed = tasks.exists() and all(not task.is_completed for task in tasks)
    
    return render(request, 'home.html', {
        'tasks': tasks,
        'all_tasks_completed': all_tasks_completed,
        'none_completed': none_completed,  # This will be True if all tasks are incomplete
    })
