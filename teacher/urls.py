from django.urls import path
from .views import teacher_added, teacher
urlpatterns = [
    path('', teacher, name="teacher"),
]
