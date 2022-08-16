import re
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth.models import User
from teacher.models import Teachers_info
# Create your views here.

# global var


def dashboard(request):
    if request.user.is_authenticated:
        db = StudentInfo.objects.all()
        user = User.objects.all()
        teacher = Teachers_info.objects.all()
        l = len(db)
        userLength = len(user)
        teacherLength = len(teacher)
        return render(request, 'dashboard/index.html', {'studentinfo': db, 'lenght': l, 'name': request.user, 'userLength': userLength, 'teacherLength': teacherLength})
    else:
        return redirect('login')


def addstudent(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Studentform(request.POST, request.FILES)
            if form.is_valid:
                form.save()
        form = Studentform()
        return render(request, 'dashboard/addstudent.html', {
            'form': form
        })
    else:
        return redirect("/login")


def student_info(request):
    if request.user.is_authenticated:
        db = StudentInfo.objects.all()
        return render(request, 'dashboard/tables.html', {'studentinfo': db})
    else:
        return redirect("/login")
# This function will Delete from database


def delete_data(request):
    data = request.POST
    id = data.get('id')
    studata = StudentInfo.objects.get(id=id)
    studata.delete()
    return redirect('/dashboard/student_table')


# this function for update sutndent data

def edit_student(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            stueditdata = StudentInfo.objects.get(id=id)
            fm = Studentform(request.POST, instance=stueditdata)
            if fm.is_valid():
                fm.save()
                return redirect('/dashboard/')
        else:
            stueditdata = StudentInfo.objects.get(id=id)
            fm = Studentform(instance=stueditdata)
        return render(request, 'dashboard/editstudent.html', {'form': fm})
    else:
        return redirect("/login")

# user information


def user(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        return render(request, 'dashboard/usertable.html', {'user': user})
    else:
        return redirect("/login")


def user_delete(request):
    data = request.POST
    id = data.get('id')
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/dashboard/user')


# teacher info


def teacher_info(request):
    if request.user.is_authenticated:
        teacher = Teachers_info.objects.all()
        return render(request, 'dashboard/teacher_table.html', {'teacher': teacher})
    else:
        return redirect('/login')


def teacher_delete(request):
    data = request.POST
    id = data.get('id')
    teacher = Teachers_info.objects.get(id=id)
    teacher.delete()
    return redirect('/dashboard/teacher_table')
