from django.http import HttpResponse, HttpResponseRedirect

from core import utils # noqa

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import get_object_or_404, render  # noqa

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student

from webargs import fields
from webargs.djangoparser import use_args


def hello(request):
    return HttpResponse('Hello!')


@use_args({
    "first_name": fields.Str(
        required=False,
    ),
    "last_name": fields.Str(
        required=False,
    ),
    "birthday": fields.Str(
        required=False,
    )
},
    location="query"
)
def get_students(request, args):
    students = Student.objects.all()
    for param_name, param_value in args.items():
        if param_value:
            students = students.filter(**{param_name: param_value})

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'students': students
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
            'form': form
        }
    )


def update_student(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'GET':
        form = StudentUpdateForm(instance=student)
    elif request.method == 'POST':
        form = StudentUpdateForm(
            data=request.POST,
            instance=student
        )
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))
          
    return render(
        request=request,
        template_name='students/update.html',
        context={
            'form': form
        }
    )


def delete_student(request, id_student):
    student = get_object_or_404(Student, id=id_student)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/delete.html',
        context={
            'student': student
        }
    )
