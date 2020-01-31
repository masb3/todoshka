from django.urls import path

from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.index, name='index'),
    path('l/<int:list_id>/', views.list, name='list'),
    path('l/<int:list_id>/u/', views.list_update, name='list_update'),
    path('t/<int:task_id>/', views.task, name='task'),
    path('newlist/', views.new_list, name='newlist'),
    path('newtask/', views.new_task, name='newtask'),
]