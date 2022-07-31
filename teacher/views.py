from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Teachers_info
from Dashboard.forms import Teacher_Form
# Create your views here.


def teacher(request):
    teacher = Teachers_info.objects.all()
    return render(request, 'teacher/teacher.html', {'teacher': teacher})


def teacher_added(request):
    if request.method == "POST":
        fm = Teacher_Form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            redirect('/dashboard')
    else:
        fm = Teacher_Form()
    return render(request, 'dashboard/teacher_add.html', {'form': fm})
