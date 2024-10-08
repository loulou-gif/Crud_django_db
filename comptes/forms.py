from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm 


class registreForm(UserCreationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={
        'class': 'form-controls ', 'placeholder' : 'Nom d\'utilisateur'
    }))
    last_name = forms.CharField( widget=forms.TextInput(attrs={
        'class': 'form-controls ', 'placeholder' : 'Nom'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-controls ', 'placeholder' : 'Prénoms'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-controls', 'placeholder' : 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-controls', 'placeholder' : 'Mot de passe'
    }))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-controls', 'placeholder' : 'Confirmer le mot de passe'
    }))
    class Meta:
        model= User
        fields= ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')
