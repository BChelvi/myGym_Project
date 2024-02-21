from django.contrib import admin
from .models import DayProgram, Exercice, Performance, ProgressUser, Series, WeekProgram, WorkoutProgram

admin.site.register(DayProgram)
admin.site.register(Exercice)
admin.site.register(Performance)
admin.site.register(ProgressUser)
admin.site.register(Series)
admin.site.register(WeekProgram)
admin.site.register(WorkoutProgram)

# Register your models here.
