from django.shortcuts import render
from django.http import HttpResponse
from .models import InnerText
from .models import TitleText
from django.template import loader


def index(request):
    header1=InnerText.objects.get(pk=1)
    header2=InnerText.objects.get(pk=2)
    header3=InnerText.objects.get(pk=3)
    header4=InnerText.objects.get(pk=4)
    header5=InnerText.objects.get(pk=5)
    header6=InnerText.objects.get(pk=6)
    header7=InnerText.objects.get(pk=7)
    header8=InnerText.objects.get(pk=8)
    header9=InnerText.objects.get(pk=9)
    header10=InnerText.objects.get(pk=10)
    TtlTxt=TitleText.objects.get(pk=1)
    TtlTxt2=TitleText.objects.get(pk=2)
    template = loader.get_template('bevprog/index.html')
    context = {
            'header1': header1,
            'header2': header2,
            'header3': header3,
            'header4': header4,
            'header5': header5,
            'header6': header6,
            'header7': header7,
            'header8': header8,
            'header9': header9,
            'header10': header10,
             'TtlTxt2': TtlTxt2,
            'TtlTxt': TtlTxt,
    }
    return HttpResponse(template.render(context, request))