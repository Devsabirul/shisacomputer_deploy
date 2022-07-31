import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from login.forms import SingUpForm, HandelLoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = HandelLoginForm(request.POST, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                user_password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    return redirect('/dashboard/')
        else:
            fm = HandelLoginForm()
        return render(request, 'login/login.html', {'form': fm})
    else:
        return redirect('/dashboard/')


def sing_up(request):
    if request.method == 'POST':
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SingUpForm()
    return render(request, 'login/register.html', {'form': fm})


def logout_(request):
    logout(request)
    return redirect('/login/')
