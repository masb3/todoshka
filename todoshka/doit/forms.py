from django import forms

from .views import List, Task


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('list_name',)


class ListUpdateForm(forms.ModelForm):
    def __init__(self, list_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['list_name'].initial = list_name

    class Meta:
        model = List
        fields = ('list_name',)


class TaskForm(forms.ModelForm):
    def __init__(self, lists=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if lists:
            self.CHOICES = []
            for _list in lists:
                self.CHOICES.append((_list.id, _list.list_name))
            self.list_name = forms.ChoiceField(choices=self.CHOICES)
            self.fields['list_name'] = self.list_name
        else:
            self.fields.pop('list_name')

    class Meta:
        model = Task
        fields = ('list_name', 'task_name',)
    list_name = forms.ChoiceField()


class TaskUpdateForm(forms.ModelForm):
    def __init__(self, lists, task, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if lists:
            self.CHOICES = []
            for _list in lists.order_by('-pub_date'):
                if task.to_list == _list:  # put on first place already related list name
                    self.CHOICES.insert(0, (_list.id, _list.list_name))
                    continue
                self.CHOICES.append((_list.id, _list.list_name))
            self.list_name = forms.ChoiceField(choices=self.CHOICES)
            self.fields['list_name'] = self.list_name
            self.fields['task_name'].initial = task.task_name
        else:
            self.fields.pop('list_name')

    class Meta:
        model = Task
        fields = ('list_name', 'task_name',)
    list_name = forms.ChoiceField()