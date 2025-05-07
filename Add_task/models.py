from django.db import models
from Category.models import Category

class Task(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True)  
    due_date = models.DateField()
    due_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title