from django.shortcuts import render
from django.http import HttpResponse
from .models import InnerText
from .models import TitleText
from django.template import loader


def index(request):
    header1=InnerText.objects.get(pk=1)
    header2=InnerText.objects.get(pk=2)
    header3=InnerText.objects.get(pk=3)
    TtlTxt=TitleText.objects.get(pk=1)
    template = loader.get_template('pocsajhu/index.html')
    context = {
            'header1': header1,
            'header2': header2,
            'header3': header3,
            
            'TtlTxt': TtlTxt,
    }
    return HttpResponse(template.render(context, request))