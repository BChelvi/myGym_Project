from django.db import models


class WeekProgram(models.Model):
    week_number = models.IntegerField()
    workout_program = models.ForeignKey('WorkoutProgram',related_name='weeks', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Week {self.week_number} of {self.workout_program}"