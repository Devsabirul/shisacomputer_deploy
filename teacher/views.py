from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Teachers_info
from Dashboard.forms import Teacher_Form
from django.contrib.auth.models import User
# Create your views here.


def teacher(request):
    if request.user.is_authenticated:
        teacher = Teachers_info.objects.all()
        return render(request, 'teacher/teacher.html', {'teacher': teacher})
    else:
        return redirect("/login")


def teacher_added(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = Teacher_Form(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                redirect('/dashboard')
        else:
            fm = Teacher_Form()
        return render(request, 'dashboard/teacher_add.html', {'form': fm})
    else:
        return redirect("/login")
