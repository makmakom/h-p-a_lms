from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all()
    obj_filter = GroupsFilter(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'obj_filter': obj_filter,
            'title': 'Groups List'
        }
    )


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm()

    return render(
        request=request,
        template_name='groups/create.html',
        context={
            'form': form,
            'title': 'Create group'
        }
    )


def update_group(request, pk):
    group = Group.objects.select_related('headman').get(id=pk)

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
            'teachers': group.teachers.select_related('group').all(),
            'students': group.students.select_related('group', 'headed_group').all(),
            'course': group.course,
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
