from django.db import models

class Prompt(models.Model):
	content = models.CharField(max_length=600)
	
class Statement(models.Model):
	prompt = models.ForeignKey(Prompt)
	message = models.CharField(max_length=1000)
	source = models.URLField(max_length=600)
	timestamp = models.DateField(auto_now=False)
	meaningcloud_sentiment_request = models.CharField(max_length=1200)
	meaningcloud_sentiment_response = models.CharField(max_length=8000)
	
class Persona(models.Model):
	statements = models.ManyToManyField(Statement)
	# values = models.ManyToManyField(Value) # This will come later.	
	
'''
This will come later.

class Value(models.Model):
	# object = ???
	# sentiment = ???

class Agenda(models.Model):
	prompts = models.ManyToManyField('prompt')
'''
