from django.forms import ModelForm

from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'age',
            'subject',
            'experience',
        ]


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'age',
            'subject',
            'experience',
        ]
