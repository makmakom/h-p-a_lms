"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from core.views import index

from lms import settings

from groups.views import create_group, get_groups

from students.views import hello

from teachers.views import create_teacher, get_teachers

urlpatterns = [
    path('', index, name='index'),
    path('', hello),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher),
    path('groups/', get_groups),
    path('groups/create/', create_group),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
