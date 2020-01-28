from django import forms

from .views import List, Task


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name',)