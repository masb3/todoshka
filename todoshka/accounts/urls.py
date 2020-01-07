from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', views.logout, name='logout'),

    #path('login/', LoginView.as_view(), name='login'),
    path('login/', views.login, name='login'),
    #path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),

    #path('changepwd/', views.changepwd, name='changepwd'),
    path('changepwd/', PasswordChangeView.as_view(template_name='accounts/changepwd.html',
                                                  success_url=reverse_lazy('doit:index')), name='changepwd'),
]