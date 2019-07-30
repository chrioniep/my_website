from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Projet, Skill

# Create your views here.

def home(request):
    projet = Projet.objects.all()
    skill = Skill.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        sujet = request.POST.get('subject')
        message = request.POST.get('message')

        
        send_mail(sujet, message, email_from, ['eponde26@gmail.com'])

    context = {
        'projet':projet,
        'skills':skill

    }
    return render(request, 'index.html', context)