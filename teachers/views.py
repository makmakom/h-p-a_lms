from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
from teachers.models import Teacher


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/delete.html',
        context={
            'teacher': teacher,
            'title': 'Delete teacher',
        }
    )


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'
    extra_context = {
        'title': 'Create teacher',
    }


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    extra_context = {
        'title': 'Teachers List',
        # 'obj_filter': TeachersFilter(data=request.GET, queryset=Teacher.objects.all()),
    }


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    extra_context = {
        'title': 'Update teacher',
    }
