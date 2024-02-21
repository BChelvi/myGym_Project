from django.db import models
from django.contrib.auth.models import User


class WorkoutProgram(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='workout_programs')
    
    def __str__(self):
        return f"Nom : {self.name}, description : {self.description}"