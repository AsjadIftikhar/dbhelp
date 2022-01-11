from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Houses, Boss


def index(request):
    houses_list = list(Houses.objects.all())
    first_boss = list(Boss.objects.all())

    context = {'housesList': houses_list,
               'firstBoss': first_boss}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
