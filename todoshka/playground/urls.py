from django.urls import path

from . import views


app_name = 'playground'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('list/<slug:unique_view_id>/', views.ListDetailView.as_view(), name='list_detail'),
]