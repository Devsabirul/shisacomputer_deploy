from django.urls import path
from .views import *
urlpatterns = [
    path('', login_, name="login"),
    path('singup', sing_up, name="sign_up"),
    path('logout', logout_, name="logout")
]
