from django.shortcuts import render, HttpResponse

from .models import Lists, Tasks


def index(request):
    lists = Lists.objects.all()
    lists_names = list()

    for l in lists:
        lists_names.append(l.list_name)

    response_html = '<br>'.join(lists_names)

    return HttpResponse(response_html)

