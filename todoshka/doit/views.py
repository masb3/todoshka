from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import List, Task
from .forms import ListForm, TaskForm


def index(request):
    lists = []
    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)

    return render(request, 'doit/index.html', {'lists': lists, })  # 'user': request.user


@login_required
def list(request, list_id):
    try:
        _list = List.objects.select_related().filter(user=request.user).get(id=list_id)
    except List.DoesNotExist:
        _list = None
    return render(request, 'doit/list.html', {'list': _list})


@login_required
def task(request, task_id):
    lists = List.objects.select_related().filter(user=request.user)
    is_task_id_valid = False
    for _list in lists:
        tasks = Task.objects.select_related().filter(to_list=_list)
        for task in tasks:
            if task.id == task_id:
                is_task_id_valid = True
                break
        if is_task_id_valid:
            break

    if is_task_id_valid:
        task = Task.objects.get(id=task_id)
    else:
        task = None

    return render(request, 'doit/task.html', {'task': task})


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
        form = TaskForm(data=request.POST, lists=lists)
        if form.is_valid():
            related_list = List.objects.get(id=request.POST['list_name'])
            newtask = form.save(commit=False)
            newtask.to_list = related_list
            newtask.save()
            return redirect('doit:index')
    else:
        form = TaskForm(lists=lists)
    return render(request, 'doit/add_list_task.html', {'form': form})