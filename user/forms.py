from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput


class SignUpForm(UserCreationForm):
    username = CharField(label="License ID", widget=TextInput(attrs={'type':'number'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name'  )
        labels = {
            'username': 'License ID',
        }
        help_texts = {

            'username': 'Please Enter Your Valid License ID'
        }