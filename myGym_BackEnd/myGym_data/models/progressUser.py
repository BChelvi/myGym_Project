from django.db import models
from django.contrib.auth.models import User

class ProgressUser(models.Model):
    user = models.ForeignKey(User,related_name='progress_user', on_delete=models.CASCADE)
    performance = models.ForeignKey('Performance',related_name='progress_user', on_delete=models.CASCADE)
    day = models.ForeignKey('DayProgram',related_name='progress_user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Progress for {self.day}"