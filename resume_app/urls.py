from django.urls import path
from .views import resume

urlpatterns = [
    path('form/', resume, name='form'),
    # path('login/', login_request, name='login'),
    # path('logout/', logout_request, name='logout')
]
