from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from app2.models import Question , Choice
from django.urls import reverse

# Create your views here.


def index(request, id1, id2):
	context={'1':id1,'2':id2}
	return render(request,'app2/index.html',context)


def home2(request, id):
	context1 = Question.objects.all()
	context = {'context':context1}
	return render(request, 'app2/home2.html', context)

def Question_choice(request, identifiant):
	handled_question = Question.objects.get(pk=identifiant)
	result_matching_request = handled_question.choice_set.all()
	context = {'one1':result_matching_request}
	return render(request, 'app2/Question.html', context)


def index2(request):
	latest_question  = Question.objects.all()
	context = {'context':latest_question}
	return render(request, 'app2/index2.html', context)



def detail(request, question_id):
	identifiant	=	Question.objects.get(pk= question_id)
	context = {'identifiant':identifiant}
	return render(request, 'app2/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app2/resultat.html', {'question':question})

def vote(request, question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request,  'app2/test.html', {'error':"ce choix n exite pas"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('results', args=(question.id,)))

def R(request, identifiant1, identifiant2, identifiant3):
	link =  request.GET.get('identifiant1')
	context = {'link':link}
	return render(request, 'app2/resultat.html', context)
