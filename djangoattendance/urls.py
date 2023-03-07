
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('welcome/', permanent=True)),
    path('welcome/', include('welcome.urls')),
    path('admin/', admin.site.urls),
    path('cv/', include('cv.urls')),
    path('projects/', include('myprojects.urls')),
    path('projects/angularproject', include('myprojects.angularproject.urls')),
    path('projects/bevprog', include('myprojects.bevprog.urls')),
    path('projects/thisproject', include('myprojects.thisproject.urls')),
    path('projects/extofirebase', include('myprojects.exceltofirebase.urls')),
    path('projects/bevprog', include('myprojects.bevprog.urls')),
    path('projects/pocsajseo', include('myprojects.pocsajhu.urls')),
]
