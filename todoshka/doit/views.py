from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import List, Task
from .forms import ListForm, TaskForm


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
    return render(request, 'doit/add_list_task.html', {'form': form})


@login_required
def new_task(request):
    lists = List.objects.select_related().filter(user=request.user)
    for _list in lists:
        tasks = Task.objects.select_related().filter(to_list=_list)

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            newtask = form.save(commit=False)
            newtask.user = request.user  # The logged-in user
            newtask.save()
            return redirect('doit:index')
        form = TaskForm(lists=lists)

    else:
        form = TaskForm(lists=lists)
    return render(request, 'doit/add_list_task.html', {'form': form})