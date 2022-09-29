from dataclasses import field
import imp
from django.forms import ModelForm
from todolist.models import Task

class addTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']