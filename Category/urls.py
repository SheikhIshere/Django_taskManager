from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_category, name='add_category'),  # Adjust function name accordingly
]
