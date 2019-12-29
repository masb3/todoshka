from django.shortcuts import render, HttpResponse

from .models import Lists, Tasks


def index(request):
    return HttpResponse("Hi!")
