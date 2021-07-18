from django.forms import ChoiceField, DateInput, ModelForm

import django_filters

from groups.models import Group


class GroupBaseForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = [
            'created_at',
            'updated_at',
        ]
        widgets = {
            'start': DateInput(attrs={'type': 'date'}),
        }


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'lessons_passed',
            'headman',
        ]


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.students.all()],
            label='Headman',
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = ['headman']


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'lessons_count': ['lt', 'gt'],
        }
