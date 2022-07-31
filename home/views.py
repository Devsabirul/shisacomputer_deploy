from django.shortcuts import render
from Dashboard.models import StudentInfo
from home.models import *
from teacher.models import Teachers_info

# Create your views here.


def home(request):
    teacher = Teachers_info.objects.all()
    return render(request, 'home/home.html', {'teacher': teacher})


def result(request):
    if request.method == 'GET':
        id = request.GET['query']
        result = StudentInfo.objects.filter(registration__icontains=id)
    return render(request, 'home/result.html', {'result': result, 'query': id})


def error_404(request, exception):
    return render(request, 'home/404.html')
