from django.urls import path
from .views import *

urlpatterns = [
    path('student',get_student,name='student')
]
