from django.urls import path, reverse_lazy
from django.conf.urls import url
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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


    path('reset/', PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done'),
                                             template_name='accounts/password_reset.html',
                                             email_template_name='accounts/password_reset_email.html',
                                             subject_template_name='accounts/password_reset_subject.txt'),
         name='password_reset'),


    path('reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),


    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete'),
                                          template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),


    path('reset/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]