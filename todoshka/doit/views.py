from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import List, Task


#@login_required
def index(request):
    lists = []
    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)

    return render(request, 'doit/index.html', {'lists': lists, })  # 'user': request.user
