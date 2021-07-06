from django.urls import path

from teachers.views import delete_teacher, get_teachers, TeacherUpdateView, TeacherCreateView

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]
