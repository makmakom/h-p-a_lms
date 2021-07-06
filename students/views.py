from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student


class StudentListView(ListView):
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


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'form': form,
            'title': 'Create student',
        }
    )


def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/delete.html',
        context={
            'student': student,
            'title': 'Delete student',
        }
    )


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
    extra_context = {
        'title': 'Update student'
    }
