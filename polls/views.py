from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from polls.forms import SignUpForm, LogInForm, ContactForm, SettingForm, MakeCourse
from polls.models import DaySelection, Article

logged_in = False
user = None


def logout(request):
    global logged_in
    logged_in = False
    return redirect('home')
    # return render(request, 'home.html', {'logged_in': logged_in})


def home(request):
    return render(request, 'home.html', {'logged_in': logged_in})


def signup(request):
    global logged_in, user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(first_name=first_name, last_name=last_name, username=username, password=raw_password)
            logged_in = True
            login(request, user)
            return redirect('home')
        else:
            error = ""
            if 'password2' in form.errors.as_data():
                error = list(form.errors.as_data()['password2'][0])[0]
            elif 'username' in form.errors.as_data():
                error = list(form.errors.as_data()['username'][0])[0]
            return render(request, 'signup.html', {'form': form, 'logged_in': logged_in, 'error': error})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'logged_in': logged_in, 'error': "nothing"})


def my_view(request):
    global logged_in, user
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logged_in = True
                login(request, user)
                return redirect('home')
            return render(request, 'login.html', {'form': form, 'logged_in': logged_in, 'error': True})

    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form, 'logged_in': logged_in})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            if 10 <= len(text) <= 250:
                send_mail(title, text + email, email, ["webe19lopers@gmail.com"], False)
                return render(request, 'contactForm.html', {'form': form, 'logged_in': logged_in, 'error': False})
            return render(request, 'contactForm.html', {'form': form, 'logged_in': logged_in, 'error': True})
    else:
        form = ContactForm()
    return render(request, 'contactForm.html', {'form': form, 'logged_in': logged_in, 'error': True})


def profile(request):
    global user
    return render(request, 'profile.html', {'user': user, 'logged_in': logged_in})


def setting(request):
    if request.method == 'POST':
        form = SettingForm(data=request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            return render(request, 'profile.html', {'user': user, 'logged_in': logged_in})
    else:
        form = SettingForm()
    return render(request, 'settingForm.html', {'form': form, 'user': user, 'logged_in': logged_in})


def panel(request):
    return render(request, 'panel.html', {'logged_in': logged_in})


def make_new_course(request):
    try:
        DaySelection.objects.create(day='0').save()
        DaySelection.objects.create(day='1').save()
        DaySelection.objects.create(day='2').save()
        DaySelection.objects.create(day='3').save()
        DaySelection.objects.create(day='4').save()
    except Exception:
        pass
    if request.method == 'POST':
        form = MakeCourse(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.start_time = instance.start_time.strptime(instance.start_time.strftime("%H:%M"), "%H:%M")
            instance.end_time = instance.end_time.strptime(instance.end_time.strftime("%H:%M"), "%H:%M")
            instance.save()
            return render(request, 'make_new_course.html', {'form': form, 'logged_in': logged_in})
    else:
        form = MakeCourse()
    return render(request, 'make_new_course.html', {'form': form, 'logged_in': logged_in})


def all_courses(request):
    courses = Article.objects.all()
    return render(request, 'all_courses.html', {'courses': courses, 'logged_in': logged_in})