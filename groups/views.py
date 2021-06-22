from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core import utils # noqa

from groups.forms import GroupCreateForm, GroupUpdateForm

from groups.models import Group

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "name": fields.Str(
        required=False,
    ),
    "lessons_count": fields.Int(
        required=False,
    ),
    "lessons_passed": fields.Int(
        required=False,
    )
},
    location="query"
)
def get_groups(request, args):
    groups = Group.objects.all()
    for param_name, param_value in args.items():
        if param_value:
            groups = groups.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'groups': groups,
            'title': 'Groups List'
        }
    )


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={
            'form': form,
            'title': 'Create group'
        }
    )
