from django.contrib import admin

# Register your models here.
from .models import Projet, Skill

admin.site.register(Projet)
admin.site.register(Skill)