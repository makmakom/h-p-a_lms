from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'
    extra_context = {
        'title': 'Create teacher',
    }


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    extra_context = {
        'title': 'Teachers List',
    }

    def get_queryset(self):
        return TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    extra_context = {
        'title': 'Update teacher',
    }


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
    extra_context = {
        'title': 'Delete teacher',
    }
