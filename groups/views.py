from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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


def update_group(request, pk):
    group = Group.objects.get(id=pk)

    if request.method == 'GET':
        form = GroupUpdateForm(instance=group)
    elif request.method == 'POST':
        form = GroupUpdateForm(
            data=request.POST,
            instance=group
        )
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={
            'form': form,
            'title': 'Update group',
        }
    )


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/delete.html',
        context={
            'group': group,
            'title': 'Delete group',
        }
    )
