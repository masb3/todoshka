from django import forms


class ListForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)