from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from polls.forms import SignUpForm, LogInForm, ContactForm


def html_start(request):
    return render(request, 'home.html', {'logged_in': False})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'home.html', {'form': form, 'logged_in': True})
        else:
            if 'password2' in form.errors.as_data():
                error = list(form.errors.as_data()['password2'][0])[0]
            elif 'username' in form.errors.as_data():
                error = list(form.errors.as_data()['username'][0])[0]
            return render(request, 'signup.html', {'form': form, 'logged_in': False, 'error': error})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'logged_in': False, 'error': "nothing"})


def my_view(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html', {'form': form, 'logged_in': True, 'error': False})
            return render(request, 'login.html', {'form': form, 'logged_in': False, 'error': True})

    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form, 'logged_in': False})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        text = form.cleaned_data['text']
        if 10 <= len(text) <= 250:
            form.save()
            return render(request, 'contactForm.html', {'form': form, 'error': False})
        return render(request, 'contactForm.html', {'form': form, 'error': True})
    else:
        form = ContactForm()
    return render(request, 'contactForm.html', {'form': form, 'error': True})
