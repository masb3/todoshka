from django.shortcuts import render, HttpResponse

from .models import List, Task


def index(request):
    lists = []
    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)

    return render(request, 'doit/index.html', {'lists': lists, })  # 'user': request.user
