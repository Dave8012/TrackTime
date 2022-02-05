import datetime
from django.contrib import admin
from django.db import models
from django import forms
from django.utils import timezone


# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class QuestionForm(forms.Form):
    text = forms.CharField(label='Question', max_length=100)
    option_1 = forms.CharField(label='Option 1', max_length=50)
    option_2 = forms.CharField(label='Option 2', max_length=50)
    option_3 = forms.CharField(label='Option 3', max_length=50)


class ChoiceForm(forms.Form):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text']

