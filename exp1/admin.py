from django.contrib import admin
from models import Prompt, Statement, Persona

class PromptAdmin(admin.ModelAdmin):
	pass	
	
admin.site.register(Prompt)

class StatementAdmin(admin.ModelAdmin):
	pass

admin.site.register(Statement)

class PersonaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Persona)

