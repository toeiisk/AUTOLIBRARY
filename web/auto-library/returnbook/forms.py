from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm
from mylibrary.models import *


class ReturnBookForm(forms.Form):
    date = forms.DateField(initial=datetime.now(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    return_date = forms.DateTimeField(initial=datetime.now(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    borrow_user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))