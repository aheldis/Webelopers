from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from polls.forms import SignUpForm, LogInForm


def html_start(request):
    return render(request, 'home.html', {'logged_in': False})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # user = User.objects.create_user(username, email, raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('/home')
            return render(request, 'home.html', {'form': form, 'logged_in': True})
    else:
        form = SignUpForm()
    return render(request, 'login.html', {'form': form, 'logged_in': False})


def my_view(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return render(request, 'home.html', {'form': form, 'logged_in': True})

    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form, 'logged_in': False})
