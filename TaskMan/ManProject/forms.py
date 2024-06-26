from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task 
        fields = ['title', 'desc', 'holder']
    
    title = forms.CharField(
        max_length=30,
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the title here',
                'class': 'form-control',
            }
        )
    )
    
    desc = forms.CharField(
        max_length=150,
        required=True,
        label='Task description',
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 30,
                'class': 'form-control',
            }
        )
    )
    
    holder = forms.CharField(
        max_length=30,
        required=True,
        label='Task Holder',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )