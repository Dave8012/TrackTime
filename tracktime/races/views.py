from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic.base import TemplateView

from .models import Schedule, Race


# Index View
class IndexView(generic.ListView):
    template_name = 'races/index.html'
    context_object_name = 'upcoming_scheduled_races'

    def get_queryset(self):
        """Returns the next upcoming Formula 1 races"""
        return Schedule.objects.order_by('date')[:1]

# Index View
# class IndexView(TemplateView):
#     template_name = 'races/index.html'


# Schedule Page View
class ScheduleView(generic.ListView):
    template_name = 'races/schedule.html'
    context_object_name = 'upcoming_scheduled_races'

    def get_queryset(self):
        """Returns any upcoming Formula 1 races"""
        return Schedule.objects.order_by('date')


# Schedule Page View
class TimesView(generic.ListView):
    template_name = 'races/times.html'
    context_object_name = 'upcoming_scheduled_races'

    def get_queryset(self):
        """Returns any upcoming Formula 1 races"""
        return Schedule.objects.order_by('date')


# Detail Page View
class DetailView(generic.DetailView):
    model = Schedule
    template_name = 'races/detail.html'


# About Page View - Using TemplateView as this is a static page
class AboutView(TemplateView):
    template_name = 'races/about.html'



