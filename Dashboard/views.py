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
        l = len(db)
        userLength = len(user)
        return render(request, 'dashboard/index.html', {'studentinfo': db, 'lenght': l, 'name': request.user, 'userLength': userLength})
    else:
        return redirect('login')


def addstudent(request):
    if request.method == "POST":
        form = Studentform(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    form = Studentform()
    return render(request, 'dashboard/addstudent.html', {
        'form': form
    })


def student_info(request):
    db = StudentInfo.objects.all()
    return render(request, 'dashboard/tables.html', {'studentinfo': db})

# This function will Delete from database


def delete_data(request):
    data = request.POST
    id = data.get('id')
    studata = StudentInfo.objects.get(id=id)
    studata.delete()
    return redirect('/dashboard/student_table')


# this function for update sutndent data

def edit_student(request, id):
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

# user information


def user(request):
    user = User.objects.all()
    return render(request, 'dashboard/usertable.html', {'user': user})


# teacher info


def teacher_info(request):
    teacher = Teachers_info.objects.all()
    return render(request, 'dashboard/teacher_table.html', {'teacher': teacher})


def teacher_delete(request):
    data = request.POST
    id = data.get('id')
    teacher = Teachers_info.objects.get(id=id)
    teacher.delete()
    return redirect('/dashboard/teacher_table')
