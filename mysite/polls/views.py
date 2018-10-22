from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .models import Question

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {
            'latest_questions': latest_questions
        })

def detail(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'polls/detail.html', {
        'question': question
    })

def results(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = Question.objects.get(pk = question_id)
    try:
        selected_choice=question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question':question, 'error_message': "Please select an option first!"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))