from django import forms 
from .models import Workflow


class WorkflowForm(forms.ModelForm):
  class Meta:
    model = Workflow
    fields = ['name', 'description', 'tags', 'status']
    







# class WorkflowForm(forms.ModelForm):
#   class Meta:
#     model = Workflow
#     fields = '__all__'
#     fields = ['name', 'description', 'retired']
#     # labels = {
#     #   'name': 'name', 
#     #   'description': 'description',
#     #   'status': 'status', 
#     #   'tags': 'tags',
#     #   'retired':'retired'
#     # }
#     # widgets = {
#     #   'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the workflow'}),
#     #   'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the description of the workflow'}),
#     #   'status': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the workflow'}),
#     #   'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the workflow'}),
#     #   'retired': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the workflow'})
      
#     # }