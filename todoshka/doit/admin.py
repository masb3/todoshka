from django.contrib import admin

from .models import List, Task


# def task_custom_action(modeladmin, request, queryset):
#     for task in queryset:
#         task.task_name = task.task_name + "__some text from custom actions"
#         task.save()
#     #queryset.update(task_name='p')


#task_custom_action.short_description = "Add some static text to task_name"


class ListAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    actions = ('task_custom_action', )

    def task_custom_action(self, request, queryset):
        for task in queryset:
            task.task_name = task.task_name + "__some text from custom actions"
            task.save()
        # queryset.update(task_name='p')

    task_custom_action.short_description = "Add some static text to task_name"


admin.site.register(List, ListAdmin)
admin.site.register(Task, TaskAdmin)
