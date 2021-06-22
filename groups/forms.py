from django.forms import DateInput, ModelForm

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'start',
            'lessons_count',
            'lessons_passed',
            'description',
        ]

        widgets = {
            'start': DateInput(attrs={'type': 'date'}),
        }


class GroupCreateForm(GroupBaseForm):
    pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        model = Group
        fields = [
            'name',
            'start',
            'lessons_count',
            'lessons_passed',
            'description',
        ]
