from django.urls import path
from .views import home, result

urlpatterns = [
    path('', home, name="HOme"),
    path('result', result, name="result"),
]
