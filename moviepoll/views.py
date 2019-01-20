from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'moviepoll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'moviepoll/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'moviepoll/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'moviepoll/detail.html', context={
            'question': question,
            'error_messages': "You didn't vote anything yet!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('moviepoll:results', args=(question.id, )))
