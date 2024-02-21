# Generated by Django 5.0.2 on 2024-02-21 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WeekProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DayProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('exercices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='myGym_data.exercice')),
                ('workout_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='myGym_data.weekprogram')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances', to='myGym_data.exercice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProgressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_user', to='myGym_data.dayprogram')),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_user', to='myGym_data.performance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_serie', models.IntegerField()),
                ('number_repetitions', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='myGym_data.performance')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('users', models.ManyToManyField(related_name='workout_programs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='weekprogram',
            name='workout_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weeks', to='myGym_data.workoutprogram'),
        ),
    ]
