from django import forms
from django.forms import fields
from .models import crud

class PostForm(forms.ModelForm):
    class Meta:
        model = crud
        fields = ['title', 'body', 'pub_date']
        widgets = {
            'pub_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }