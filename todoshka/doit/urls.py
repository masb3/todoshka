from django.urls import path

from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.index, name='index'),
]