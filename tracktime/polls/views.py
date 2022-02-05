from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext
import datetime

from .models import Choice, Question, QuestionForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = QuestionForm()
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def submit_question(request):

    if request.method == 'POST':

        form = QuestionForm(request.POST)

        if form.is_valid():

            text = form.cleaned_data['text']
            option_1 = form.cleaned_data['option_1']
            option_2 = form.cleaned_data['option_2']
            option_3 = form.cleaned_data['option_3']
            option_list = [option_1, option_2, option_3]
            q = Question(question_text=text, pub_date=datetime.datetime.now())
            q.save()
            print(q.pk)

            for option in option_list:
                print(option)
                c = Choice(question=q, choice_text=option, votes=0)
                c.save()

            return HttpResponseRedirect(reverse('polls:index'))

    else:
        form = QuestionForm()

    return render(request, 'polls/index.html', {'form': form})




