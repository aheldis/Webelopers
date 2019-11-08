from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from polls.models import DaySelection, Article


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)


class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class ContactForm(forms.Form):
    title = forms.CharField(required=False)
    email = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)


class SettingForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)


class MakeCourse(ModelForm):
    first_day = forms.ModelChoiceField(DaySelection.objects.all())
    second_day = forms.ModelChoiceField(DaySelection.objects.all())

    class Meta:
        model = Article
        fields = ['department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time']
