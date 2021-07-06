from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

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


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'
    extra_context = {
        'title': 'Update group',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = self.get_object().teachers.all()
        context['students'] = self.get_object().students.select_related('group', 'headed_group').all()
        context['course'] = self.get_object().course

        return context
