import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone


# Races Models

# Schedule model
class Schedule(models.Model):
    race_name = models.CharField(max_length=100)
    date = models.DateField('race date')

    def __str__(self):
        return self.race_name

    @admin.display(
        boolean=True,
        ordering='date',
        description='Upcoming Race?',
    )
    def is_upcoming_soon(self):
        # return timezone.now().date() <= self.date <= timezone.now().date() + datetime.timedelta(days=10)
        return self.date >= timezone.now().date()


# Race model
class Race(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    time = models.DateTimeField('race time')

    def __str__(self):
        return self.location
