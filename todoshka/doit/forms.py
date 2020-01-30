from django import forms

from .views import List, Task


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name',)


class TaskForm(forms.ModelForm):
    def __init__(self, lists=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if lists:
            self.CHOICES = []
            for list in lists:
                self.CHOICES.append((list.id, list.list_name))
            self.list_name = forms.ChoiceField(choices=self.CHOICES)
            self.fields['list_name'] = self.list_name
        else:
            self.fields.pop('list_name')

    class Meta:
        model = Task
        fields = ('list_name', 'task_name',)
    list_name = forms.ChoiceField()
