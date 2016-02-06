from django import forms
from django.forms import PasswordInput


class AuthForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'username', 'autofocus':'autofocus'}))
    password = forms.CharField(max_length=50, widget=PasswordInput(attrs={'placeholder': 'password'}))
