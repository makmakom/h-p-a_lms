from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'
    extra_context = {
        'title': 'Create student',
    }


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/list.html'
    extra_context = {
        'title': 'Student list'
    }

    def get_queryset(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
    extra_context = {
        'title': 'Update student'
    }


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
    extra_context = {
        'title': 'Delete student',
    }
