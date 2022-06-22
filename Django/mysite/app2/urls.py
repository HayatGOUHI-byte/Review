from django.contrib import admin
from django.urls import path
from app2 import views


#revoir la facon de mettre des Urls , commence par le premier url puis parcours la liste

urlpatterns = [
   path('<int:id1>/<int:id2>', views.index, name="index"),
   path('home2/<int:id>', views.home2, name="home"),
   path('home3/<int:identifiant>', views.Question_choice, name="question"),
   path('', views.index, name='index'),
   path('index2/', views.index2, name='index2'),
    # ex: /polls/5/
   path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
   path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
   path('<int:question_id>/vote/', views.vote, name='vote'),
   path('resultat/<int:identifiant1>/<int:identifiant2>/<int:identifiant3>', views.R, name="Res"),

       
]
