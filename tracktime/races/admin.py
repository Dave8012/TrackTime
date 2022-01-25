from django.contrib import admin
from .models import Schedule, Race


# Schedule Model Admin Configuration
class ScheduleAdmin(admin.ModelAdmin):
    ordering = ['date']
    list_display = ('race_name', 'date', 'is_upcoming_soon')


# Race Model Admin Configuration
class RaceAdmin(admin.ModelAdmin):
    ordering = ['time']
    list_display = ('schedule', 'location', 'time')


# Registering Models on the Admin Page
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Race, RaceAdmin)
