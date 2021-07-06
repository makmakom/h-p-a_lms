from courses.views import create_course, delete_course, get_courses, update_course

from django.urls import path

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course, name='create'),
    path('update/<int:pk>/', update_course, name='update'),
    path('delete/<int:pk>/', delete_course, name='delete'),
]
