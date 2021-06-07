from django.http import HttpResponse
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
        missing='',
    ),
    "last_name": fields.Str(
        required=False,
        missing='',
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
        students = students.filter(**{param_name: param_value})

    records = format_records(students)
    return HttpResponse(records)


def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(str(elem) for elem in lst)
