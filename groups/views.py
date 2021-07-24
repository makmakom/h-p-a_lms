from copy import copy

from django.contrib import messages
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

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'Group {form.cleaned_data["name"]} was successfully created.')

        return result


class GroupListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    model = Group
    template_name = 'groups/list.html'
    extra_context = {
        'title': 'Groups List'
    }

    def get_filter(self):
        return GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.select_related('headman', 'course').prefetch_related('students').all()
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']

        context['get_params'] = params.urlencode()

        return context


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

    def delete(self, *args, **kwargs):
        result = super(DeleteView, self).delete(*args, **kwargs)
        messages.info(self.request, 'Group was successfully deleted.')

        return result
