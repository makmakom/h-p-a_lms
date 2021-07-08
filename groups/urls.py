from django.urls import path

from groups.views import GroupUpdateView, create_group, delete_group, get_groups

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:pk>/', GroupUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]
