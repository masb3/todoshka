from django.shortcuts import render, HttpResponse

from .models import List, Task


def index(request):
    lists = List.objects.all()

    return render(request, 'doit/index.html', {'lists': lists, })  # 'user': request.user
