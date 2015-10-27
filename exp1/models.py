from django.db import models

class Persona(models.Model):
	statements = models.ManyToManyField('Statement')
	# values = models.ManyToManyField('value') # This will come later.

class Prompt(models.Model):
	content = CharField()
	
class Statement(models.Model):
	prompt = models.ForeignKey('Prompt')
	message = CharField()
	source = URLField(max_length=600)
	timestamp = DateField(auto_now=False)
	meaningcloud_sentiment_request = CharField()
	meaningcloud_sentiment_response = CharField()
	
'''
This will come later.

class Value(models.Model):
	# object = ???
	# sentiment = ???

class Agenda(models.Model):
	prompts = models.ManyToManyField('prompt')
'''
