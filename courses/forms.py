from courses.models import Course

from django.forms import ModelForm

import django_filters


class CourseBaseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = [
            'created_at',
            'updated_at',
        ]


class CourseCreateForm(CourseBaseForm):
    pass


class CourseUpdateForm(CourseBaseForm):
    pass


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains'],
        }
