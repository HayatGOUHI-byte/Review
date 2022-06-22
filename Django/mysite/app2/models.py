from django.db import models

# Create your models here.


#une question a plusieurs choix c'est ca  A = 12 , A = 13, A = 14

class Question(models.Model):
	Question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date_published')


class Choice(models.Model):
	question = models.ForeignKey(Question,	on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
