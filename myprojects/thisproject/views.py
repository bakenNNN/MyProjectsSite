from django.shortcuts import render
from django.http import HttpResponse
from .models import InnerText
from .models import TitleText
from django.template import loader


def index(request):
    header1=InnerText.objects.get(pk=1)
   
    TtlTxt=TitleText.objects.get(pk=1)
    template = loader.get_template('thisproject/index.html')
    context = {
            'header1': header1,
            
            'TtlTxt': TtlTxt,
    }
    return HttpResponse(template.render(context, request))