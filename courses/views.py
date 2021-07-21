from courses.forms import CourseCreateForm, CourseFilter, CourseUpdateForm
from courses.models import Course

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'
    extra_context = {
        'title': 'Create course',
    }


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/list.html'
    extra_context = {
        'title': 'Courses List',
    }

    def get_queryset(self):
        return CourseFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'
    extra_context = {
        'title': 'Update course',
    }


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
    extra_context = {
        'title': 'Delete course',
    }
