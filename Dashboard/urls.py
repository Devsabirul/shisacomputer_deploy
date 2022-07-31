from re import T
from django.urls import path
from .views import dashboard, addstudent, student_info, delete_data, edit_student, user, teacher_info, teacher_delete
from teacher.views import teacher_added
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", dashboard, name="Dashboard"),
    path('addstudent', addstudent, name="Add Student"),
    path('student_table', student_info, name="student_info"),
    path('user', user, name="user"),
    path('teacher_add', teacher_added, name="teacher_added"),
    path('teacher_table', teacher_info, name="teacher_info"),
    path('delete', delete_data, name="delete_data"),
    path('teacher_delete', teacher_delete, name="teacher_delete"),
    path('<id>', edit_student, name="edit_student"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
