from django.forms import ModelForm

from groups.models import Group


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'start', 'lessons_count', 'lessons_passed']
