from django.urls import path

from students.views import create_student, delete_student, get_students, update_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:pk>/', update_student, name='update'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
