from copy import copy

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'
    extra_context = {
        'title': 'Create student',
    }

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'Student {form.cleaned_data["first_name"]} was successfully created.')

        return result


class StudentListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    model = Student
    template_name = 'students/list.html'
    extra_context = {
        'title': 'Student list'
    }

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.select_related('group', 'headed_group').all()
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


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
    extra_context = {
        'title': 'Update student'
    }


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
    extra_context = {
        'title': 'Delete student',
    }

    def delete(self, *args, **kwargs):
        result = super(DeleteView, self).delete(*args, **kwargs)
        messages.info(self.request, 'Student was successfully deleted.')

        return result
