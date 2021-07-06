from django.urls import path

from teachers.views import create_teacher, delete_teacher, get_teachers, TeacherUpdateView

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]
