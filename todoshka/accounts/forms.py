from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=False, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LogInForm(AuthenticationForm):
    pass


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()