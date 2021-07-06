from django.urls import path

from students.views import StudentUpdateView, create_student, delete_student, StudentListView

app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
