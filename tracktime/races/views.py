from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Schedule


class IndexView(generic.ListView):
    template_name = 'races/index.html'
    context_object_name = 'upcoming_scheduled_races'

    def get_queryset(self):
        """Returns any upcoming Formula 1 races"""
        # return Schedule.objects.order_by('-date')[:5]
        return Schedule.objects.order_by('date')


class DetailView(generic.DetailView):
    model = Schedule
    template_name = 'races/detail.html'

