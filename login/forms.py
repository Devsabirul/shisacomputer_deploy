from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class SingUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class HandelLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Email Address...'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'}))

    error_messages = {
        "invalid_login":(
            "Please enter a correct %(username)s and password."
        )
    }
