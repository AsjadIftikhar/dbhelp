from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Houses, Boss


def index(request):
    houses_list = Houses.objects.all()
    all_boss = Boss.objects.all()
    boss = None
    for b in all_boss:
        boss = b
        break

    percentage = (boss.hp / boss.max_hp)*100

    context = {'houses_list': houses_list,
               'boss': boss,
               'percentage': percentage}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
