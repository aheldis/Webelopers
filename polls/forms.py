from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from polls.models import Message


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password', )


class ContactForm(forms.Form):
    title = forms.CharField(required=False)
    email = forms.CharField(required=False)
    text = forms.CharField(required=False)

    class Meta:
        model = Message
        fields = ('title', 'email', 'text')
