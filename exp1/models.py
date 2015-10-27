from django.db import models

class Prompt(models.Model):
	content = CharField(max_length=600)
	
class Statement(models.Model):
	prompt = models.ForeignKey(Prompt)
	message = CharField(max_length=1000)
	source = URLField(max_length=600)
	timestamp = DateField(auto_now=False)
	meaningcloud_sentiment_request = CharField(max_length=1200)
	meaningcloud_sentiment_response = CharField(max_length=8000)
	
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
