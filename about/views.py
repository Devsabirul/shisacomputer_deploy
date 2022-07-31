from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def about_us(request):
    # return HttpResponse("This is about")
    return render(request, 'about_us/index.html')
