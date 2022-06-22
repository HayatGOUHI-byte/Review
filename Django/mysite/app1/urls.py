from django.contrib import admin
from django.urls import path
from app1 import views
from app1.models import Article, Reporter


urlpatterns = [
   path('home/', views.Home, name="home"),
   path('disReporter', views.DisReporter, name="disReporter"),
   path('index/<int:id>/', views.index, name="index"),
   path('home/articles/<int:id>/', views.year_archive, name="article"),
   path('home/<int:year>/<int:month>/<int:day>/', views.article_details, name="function")
       
]
