from django.db.models import F
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
import pytz
# Create your views here.


# We started by defining a function to generate an index view like so:
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# We're now changing to a class of objects to use Django's
# 'generic' views, to reduce code redundancy as follows:
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



# We started by defining a function to generate a detail view like so:
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
# We're now changing to a class of objects to use Django's
# 'generic' views, to reduce code redundancy as follows:
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# We started by defining a function to generate a results view like so:
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
# We're now changing to a class of objects to use Django's
# 'generic' views, to reduce code redundancy as follows:
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
        # The F('votes') avoids a 'race condition' by preventing
        # votes from being counted once if two people vote at the
        # exact same time, as opposed to two.
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def potato(request, question_id):
    response = "You're a potato. You shouldn't be able to comprehend %s."
    return HttpResponse(response % question_id)


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})