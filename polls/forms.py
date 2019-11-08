from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password', )


class ContactForm(forms.Form):
    text = forms.CharField(min_length=10, max_length=250, required=False)

    class Meta:
        fields = ('title', 'email', 'text')
