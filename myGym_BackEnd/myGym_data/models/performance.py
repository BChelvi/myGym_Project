from django.db import models
from django.contrib.auth.models import User

class Performance(models.Model):
    user = models.ForeignKey(User,related_name='performances', on_delete=models.CASCADE)
    exercice = models.ForeignKey('Exercice',related_name='performances', on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user.username}'s Performance on {self.date}"