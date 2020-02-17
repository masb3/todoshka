from django.shortcuts import render, HttpResponse
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

from doit.models import List, Task

from .forms import ListForm


class IndexView(TemplateView):
    template_name = 'playground/playground.html'

    def get(self, request, *args, **kwargs):
        req = request.GET

        if request.GET:
            ret = ""
            for key in req:
                ret += "key = {}, val = {}<br>".format(key, request.GET.get(key))
        else:
            ret = "None"

        return HttpResponse(ret)


class ListView(ListView):
    template_name = 'playground/list.html'
    context_object_name = 'list_of_lists'

    def get_queryset(self):
        return List.objects.select_related().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.select_related().filter(user=self.request.user)
        return context


class ListDetailView(DetailView):
    template_name = 'playground/list_detail.html'
    #   context_object_name = 'aaaa'

    # def get_queryset(self):
    #     return List.objects.select_related().filter(user=self.request.user)

    def get_object(self, queryset=None):
        self.context_object_name = 'aaaa'
        print(List.objects.get(unique_view_id=self.kwargs['unique_view_id']))
        return List.objects.get(unique_view_id=self.kwargs['unique_view_id'])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.pop('object')
    #     return context


class ListFormView(FormView):
    template_name = 'playground/form.html'
    form_class = ListForm
    success_url = reverse_lazy('playground:list')
