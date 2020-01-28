from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import List, Task
from .forms import ListForm


#@login_required
def index(request):
    lists = []
    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)

    return render(request, 'doit/index.html', {'lists': lists, })  # 'user': request.user


@login_required
def new_list(request):
    if request.method == 'POST':
        form = ListForm(data=request.POST)
        if form.is_valid():
            newlist = form.save(commit=False)
            newlist.user = request.user  # The logged-in user
            newlist.save()
            return redirect('doit:index')
    else:
        form = ListForm()
    return render(request, 'doit/newlist.html', {'form': form})
