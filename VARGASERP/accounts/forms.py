from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    CHOICES=[('vendedor','Vendedor'), ('admin','Admin')]
    group = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']