from django.contrib import admin
from .models import InnerText
from .models import TitleText
admin.site.register(TitleText)
admin.site.register(InnerText)