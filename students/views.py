from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm, StudentUpdateForm
from students.models import Student
from django.shortcuts import render

from webargs.djangoparser import use_args
from webargs import fields


# Create your views here.


def hello(request):
    return HttpResponse('Hello!')


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
            'students': students
        }
    )


@csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()

    elif request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/students/')

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'form': form
        }
    )


@csrf_exempt
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

            return HttpResponseRedirect('/students/')

    return render(
        request=request,
        template_name='students/update.html',
        context={
            'form': form
        }
    )
