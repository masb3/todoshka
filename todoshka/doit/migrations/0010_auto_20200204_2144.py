# Generated by Django 2.2.8 on 2020-02-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doit', '0009_task_unique_view_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='unique_view_id',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
