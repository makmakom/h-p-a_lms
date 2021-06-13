import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput

from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'birthday',
            'enroll_date',
            'graduate_date',
        ]
        # fields = '__all__'
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
            'enroll_date': DateInput(attrs={'type': 'date'}),
            'graduate_date': DateInput(attrs={'type': 'date'})
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

    # def clean_birthday(self):
    #     birthday = self.cleaned_data['birthday']
    #     age = datetime.datetime.now().year - birthday.year
    #     if age < 18:
    #         raise ValidationError('Age should bee grater then 18 y.o.')
    #
    #     return birthday

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
            'birthday',
            'enroll_date',
            'graduate_date',
        ]
