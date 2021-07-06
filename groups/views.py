from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Group
from students.models import Student


# def get_groups(request):
#     groups = Group.objects.all()
#     obj_filter = GroupsFilter(data=request.GET, queryset=groups)
#
#     return render(
#         request=request,
#         template_name='groups/list.html',
#         context={
#             'obj_filter': obj_filter,
#             'title': 'Groups List'
#         }
#     )


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'
    extra_context = {
        'title': 'Create group'
    }


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    extra_context = {
        'title': 'Groups List'
    }


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

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.id
        except AttributeError as ex:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.headman = Student.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return response


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
    extra_context = {
        'title': 'Delete group'
    }
