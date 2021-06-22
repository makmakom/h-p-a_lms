from django.urls import path

from teachers.views import create_teacher, get_teachers

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
]
