import re

import django_filters
from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'birthday',
            'enroll_date',
            'graduate_date',
        ]
        # fields = '__all__'
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
            'enroll_date': DateInput(attrs={'type': 'date'}),
            'graduate_date': DateInput(attrs={'type': 'date'}),
            'phone_number': DateInput(attrs={
                'type': 'phone',
                'placeholder': '+38 000 132-4567',
                'pattern': r'\+[0-9]{2} [0-9]{3} [0-9]{3}-[0-9]{4}',
            })
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

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        return '+' + re.sub(r'[^\d]', '', phone)

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date couldn\'t be greater than graduate date!')


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birthday',
            'enroll_date',
            'graduate_date',
        ]


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
