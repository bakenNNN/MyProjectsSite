from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    welcT="this is myprojects page"
    template = loader.get_template('myprojects/projects.html')
    context = {
            'welcT': welcT,
    }
    return HttpResponse(template.render(context, request))