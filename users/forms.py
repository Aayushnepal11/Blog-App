from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class CustomUserCreation(UserCreationForm):
    User = get_user_model()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'password1', 'password2')
