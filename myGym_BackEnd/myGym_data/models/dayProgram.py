from django.db import models


class DayProgram(models.Model):
    day_number = models.IntegerField()
    workout_week = models.ForeignKey('WeekProgram',related_name='days', on_delete=models.CASCADE)
    exercises = models.ManyToManyField('Exercice', related_name='day_programs')
    
    def __str__(self):
        return f"Day {self.day_number} of Week {self.workout_week.week_number} of Program {self.workout_week.workout_program}"