from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import List, Task
from .forms import ListForm, TaskForm, ListUpdateForm,TaskUpdateForm


def index(request):
    lists = None
    if request.user.is_authenticated:
        list_of_lists = List.objects.filter(user=request.user).order_by('-pub_date')
        page = request.GET.get('page', 1)
        paginator = Paginator(list_of_lists, 3)
        try:
            lists = paginator.page(page)
        except PageNotAnInteger:
            lists = paginator.page(1)
        except EmptyPage:
            lists = paginator.page(paginator.num_pages)

    return render(request, 'doit/index.html', {'lists': lists, })


@login_required
def list(request, list_id):
    try:
        _list = List.objects.select_related().filter(user=request.user).get(id=list_id)
    except List.DoesNotExist:
        _list = None
    return render(request, 'doit/list.html', {'list': _list})


@login_required
def list_update(request, list_id):
    try:
        _list = List.objects.select_related().filter(user=request.user).get(id=list_id)

        if request.method == 'POST':
            if 'true' == request.POST.get('delete'):
                _list.delete()
                return redirect('doit:index')
            else:  # update
                form = ListUpdateForm(data=request.POST, list_name=_list.list_name)
                if form.is_valid():
                    _list.list_name = request.POST['list_name']
                    _list.save(update_fields=["list_name"])
                    return redirect('doit:index')
        else:
            form = ListUpdateForm(list_name=_list.list_name)

    except List.DoesNotExist:
        form = None

    return render(request, 'doit/list_task_update_delete.html', {'form': form})


def get_task_util(request, task_id):
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

    return task


@login_required
def task(request, task_id):
    task = get_task_util(request, task_id)

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


@login_required
def task_update(request, task_id):
    task = get_task_util(request, task_id)

    if request.method == 'POST':
        if 'true' == request.POST.get('delete'):
            task.delete()
            return redirect('doit:index')
        else:
            lists = List.objects.select_related().filter(user=request.user)
            form = TaskUpdateForm(data=request.POST, task=task, lists=lists)
            if form.is_valid():
                related_list = List.objects.get(id=request.POST['list_name'])
                task.to_list = related_list
                task.task_name = request.POST['task_name']
                task.save(update_fields=["to_list", "task_name"])
                return redirect('doit:index')

    else:
        lists = List.objects.select_related().filter(user=request.user)
        form = TaskUpdateForm(task=task, lists=lists)

    return render(request, 'doit/list_task_update_delete.html', {'form': form})
