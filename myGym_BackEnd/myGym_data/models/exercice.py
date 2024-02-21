from django.db import models

class Exercice(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name