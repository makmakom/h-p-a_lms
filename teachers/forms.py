import re

from django.forms import DateInput, ModelForm

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'age',
            'subject',
            'experience',
        ]
        widgets = {
            'phone_number': DateInput(attrs={
                'type': 'phone',
                'placeholder': '+38 000 132-45-67'
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


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'age',
            'subject',
            'experience',
        ]
