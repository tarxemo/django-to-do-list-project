from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 bg-gray-800 border-gray-700 text-white',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 bg-gray-800 border-gray-700 text-white',
                'rows': 3,
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 bg-gray-800 border-gray-700 text-white',
            }),
        }

from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 bg-gray-700 border-gray-600 text-white'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 bg-gray-700 border-gray-600 text-white'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500 bg-gray-700 border-gray-600 text-white'
        })