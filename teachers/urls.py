from django.urls import path

from teachers.views import delete_teacher, TeacherUpdateView, TeacherCreateView, TeacherListView

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]
