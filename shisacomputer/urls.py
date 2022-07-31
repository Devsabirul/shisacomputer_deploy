from django.contrib import admin
from django.urls import path, include
from about.views import about_us
from course.views import courses
from teacher.views import teacher
from blog.views import blog
from contact.views import contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about_us', about_us, name="About_us"),
    path("courses", courses, name="courses"),
    path('teacher', include('teacher.urls')),
    path('blog', blog, name="blog"),
    path('contact', contact, name="contact"),
    path('dashboard/', include('Dashboard.urls')),
    path('login/', include('login.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'home.views.error_404'
