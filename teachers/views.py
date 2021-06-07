from django.http import HttpResponse
from webargs import fields, validate
from webargs.djangoparser import use_args
from teachers.models import Teacher


@use_args({
    "first_name": fields.Str(
        required=False,
    ),
    "last_name": fields.Str(
        required=False,
    ),
    "age": fields.Int(
        required=False,
        validate=[validate.Range(min=1, max=99)]
    ),
    "subject": fields.Str(
        required=False,
    ),
    "experience": fields.Str(
        required=False,
    )
},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    for param_name, param_value in args.items():
        if param_name == 'experience':
            teachers = teachers.filter(**{f'{param_name}__contains': param_value})
        else:
            teachers = teachers.filter(**{param_name: param_value})

    records = format_records(teachers)
    return HttpResponse(records)


# todo: need to move to Utils
def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(str(elem) for elem in lst)
