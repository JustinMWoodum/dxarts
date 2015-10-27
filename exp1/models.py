from django.db import models

class Persona(models.Model):
	statements = models.ManyToManyField('statement')
	# values = models.ManyToManyField('value') # This will come later.

class Prompt(models.Model):
	content = CharField(max_length=None)
	
class Statement(models.Model):
	prompt = models.ForeignKey('prompt')
	message = CharField(max_length=None)
	source = URLField(max_length=600)
	timestamp = DateField(auto_now=False)
	meaningcloud_sentiment_request = CharField(max_length=None)
	meaningcloud_sentiment_response = CharField(max_length=None)
	
'''
This will come later.

class Value(models.Model):
	# object = ???
	# sentiment = ???

class Agenda(models.Model):
	prompts = models.ManyToManyField('prompt')
'''
