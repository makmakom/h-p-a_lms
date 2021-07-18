from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Group

from students.models import Student


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'
    extra_context = {
        'title': 'Create group'
    }


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups/list.html'
    extra_context = {
        'title': 'Groups List'
    }

    def get_queryset(self):
        return GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )


class GroupUpdateView(LoginRequiredMixin, UpdateView):
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


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'
    extra_context = {
        'title': 'Delete group'
    }
