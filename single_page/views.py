from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import houses, boss


def index(request):
    houses_list = houses.objects.all()
    all_boss = boss.objects.all()
    bos = None
    for b in all_boss:
        bos = b
        break

    percentage = (bos.hp / bos.maxhp) * 100

    context = {'houses_list': houses_list,
               'boss': bos,
               'percentage': percentage}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
