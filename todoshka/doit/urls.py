from django.urls import path

from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.index, name='index'),
    path('l/<slug:list_id>/', views.list, name='list'),
    path('l/<slug:list_id>/u/', views.list_update, name='list_update'),
    path('t/<slug:task_id>/', views.task, name='task'),
    path('t/<slug:task_id>/u', views.task_update, name='task_update'),
    path('newlist/', views.new_list, name='newlist'),
    path('newtask/', views.new_task, name='newtask'),
]