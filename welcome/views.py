from django.shortcuts import render
from django.http import HttpResponse
from .models import WelcomeText
from django.template import loader


def index(request):
    welcT=WelcomeText.objects.get(pk=1)
    template = loader.get_template('welcome/index.html')
    context = {
            'welcT': welcT,
    }
    return HttpResponse(template.render(context, request))

