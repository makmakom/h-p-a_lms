from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

import django_filters

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = [
            'created_at',
            'updated_at',
        ]
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'}),
            'enroll_date': DateInput(attrs={'type': 'date'}),
            'graduate_date': DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self.normalize_name(last_name)

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date couldn\'t be greater than graduate date!')


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    pass


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
