from django.forms import DateInput, ModelForm

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
    pass


class GroupUpdateForm(GroupBaseForm):
    pass


class GroupsFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['exact', 'icontains'],
            'lessons_count': ['lt', 'gt'],
        }
