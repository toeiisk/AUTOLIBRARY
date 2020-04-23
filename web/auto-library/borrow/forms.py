from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm, TextInput, Select
from mylibrary.models import *
from django.contrib.auth.models import User


class BorrowNotesForm(forms.Form):
    date = forms.DateField(initial=datetime.now(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    return_date = forms.DateTimeField(initial=datetime.now()+timedelta(days=7), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    borrow_user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))

class BorrowComForm(forms.ModelForm):
    class Meta:
        model = Borrower_Computer
        fields = ('date', 'expire_date')
        widgets = {
            'date': TextInput(attrs={'class': 'form-control mb-5'}),
            'expire_date': TextInput(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
        "date": "DATE",
        "expire_date": "EXPIRE_DATE",
    }


class BorrowTutorForm(forms.ModelForm):
    class Meta:
        model = Borrower_Tutor_Room
        fields = ('date', 'expire_date')
        widgets = {
            'date': TextInput(attrs={'class': 'form-control mb-5'}),
            'expire_date': TextInput(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
        "date": "DATE",
        "expire_date": "EXPIRE_DATE",
    }