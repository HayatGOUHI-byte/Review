from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from app1.models import Article, Reporter
from datetime import datetime

def index(request, id):
	current_journalist = Article.objects.get(pk = id)
	dic = {'cle1' : "bonjour notre journalist ", 'cle2' : "bonsoir notre journalist ", 'current' : datetime.now(),
	'name_journalist' : current_journalist,'id':id
 	}
	return render(request, 'app1/index.html', dic)

def Home(request):
    context =  {
	"one" : Article.objects.all(),
	"two" : Reporter.objects.all(),
	"third" : "jaguar"
    }
    return render(request, 'app1/Home.html', context)

def DisReporter(request):
	context = Reporter.objects.values()
	Reporter_dic = {
	'context1' : context
	}
	return render(request,'app1/DisReporter.html', Reporter_dic)

def year_archive(request, id):
	a_list = Reporter.objects.get(pk=id)
	context = {'year': id, 'article_list': a_list}
	return render(request, 'app1/ArticleArchivee.html', context)

def article_details(request, year, month, day):
	ArticlNBCNews = Article.objects.filter(pub_date = datetime(year, month, day))
	context={'Article_magique':ArticlNBCNews,'year1':year,'month1':month,'day1':day}
   
	return render(request, 'app1/ArticleArchivee.html', context)
