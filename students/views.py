from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core import utils # noqa

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "first_name": fields.Str(
        required=False,
    ),
    "last_name": fields.Str(
        required=False,
    ),
    "birthday": fields.Date(
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
            'students': students,
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


def update_student(request, id):
    student = Student.objects.get(id=id)

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
            'form': form,
            'title': 'Update student',
        }
    )
