from django.db import models


class Reporter(models.Model):
	full_name = models.CharField(max_length = 70)
   

	def __self__(self):
		return self.full_name

	def name(self):
		return "hello".self.full_name


class Article(models.Model):
	pub_date = models.DateField()
	headline = models.CharField(max_length = 200)
	content = models.TextField()
	Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __self__(self):
		return self.headline

	

