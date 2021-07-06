from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student


def get_students(request):
    students = Student.objects.all().select_related('group')
    obj_filter = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'obj_filter': obj_filter,
            'title': 'Students list',
        }
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
