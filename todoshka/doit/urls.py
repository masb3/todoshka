from django.urls import path

from . import views

app_name = 'doit'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<int:list_id>/', views.list, name='list'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('newlist/', views.new_list, name='newlist'),
    path('newtask/', views.new_task, name='newtask'),
]