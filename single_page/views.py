from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import houses,boss



def index(request):

    housesList = list(houses.objects.all())
    firstBoss = list(boss.objects.all())

    context = {'housesList': housesList,
               'firstBoss': firstBoss[0]}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


