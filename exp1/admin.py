from django.contrib import admin
from .models import Prompt, Statement, Persona
	
admin.site.register(Prompt)
admin.site.register(Statement)
admin.site.register(Persona)

