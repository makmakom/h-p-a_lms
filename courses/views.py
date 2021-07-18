from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from courses.forms import CourseCreateForm, CourseFilter, CourseUpdateForm
from courses.models import Course

from django.urls import reverse_lazy


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'
    extra_context = {
        'title': 'Create course',
    }


class CourseListView(ListView):
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


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'
    extra_context = {
        'title': 'Update course',
    }


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
    extra_context = {
        'title': 'Delete course',
    }
