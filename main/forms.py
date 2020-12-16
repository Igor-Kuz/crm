from django.forms import ModelForm, DateInput, TextInput,HiddenInput,Textarea,CheckboxSelectMultiple
from .models import *
from django.contrib.auth.models import User

class SpaceForm(ModelForm):
	class Meta:
		model = Space
		fields = ('name', 'photo', 'assign', 'status', 'created_by', 'color')
		widgets = {
			'color': TextInput(attrs={'type':'color'})
		}
		


class ListForm(ModelForm):
	class Meta:
		model = List
		fields = ('space','name_list',)

class TaskForm(ModelForm):
	class Meta:
		model = Task
		due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)
		fields = ['lists','task_name', 'assign', 'dead_line', 'attachments', 'status', 'description','created_by', 'due']
		widgets = {
			'lists':HiddenInput(),
			'dead_line': DateInput(attrs={'type': 'date'}),
			'assign': CheckboxSelectMultiple()
		}
		

class SubTaskForm(ModelForm):
	class Meta:
		model = SubTask
		fields = ('task','task_name', 'assign', 'dead_line', 'attachments', 'status', 'description',  'created_by')

		widgets = {
			'task':HiddenInput(),
			'dead_line': DateInput(attrs={'type': 'date'}),
		}

class TaskCommentForm(ModelForm):
	class Meta:
		model = TaskComment
		fields = ('task','name', 'comment')
		widgets = {
			'task': HiddenInput(),
			'name': HiddenInput(),
			'comment': Textarea(attrs = {'class': 'form-control comment-area'})
		}

