from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm, TextInput, Select
from mylibrary.models import *
from django.contrib.auth.models import User


class BorrowNotesForm(forms.ModelForm):
    class Meta:
        model = Borrow_Notes
        fields = ('date', 'return_date')
        widgets = {
            'date': TextInput(attrs={'class': 'form-control mb-5'}),
            'return_date': TextInput(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
        "date": "DATE",
        "return_date": "RETURN_DATE",
    }
   

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