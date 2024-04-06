from django.urls import path
from .views import resume, login_request, logout_request, register_request, home

urlpatterns = [
    path('', home, name='home'),
    path('form/', resume, name='form'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_request, name='register')
]
