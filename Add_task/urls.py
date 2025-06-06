from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # This will show all tasks
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/', views.task_details, name='task_details'),
]