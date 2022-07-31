from dataclasses import fields
from logging import PlaceHolder
from django import forms
from .models import *
from teacher.models import Teachers_info


class Studentform(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"
        widgets = {
            'registration': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phoneNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'courses': forms.TextInput(attrs={'class': 'form-control'}),
            'certificate': forms.FileInput(attrs={'class': 'form-control'}),
        }

class Teacher_Form(forms.ModelForm):
    class Meta:
        model = Teachers_info
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'skill':forms.TextInput(attrs={'class':'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }