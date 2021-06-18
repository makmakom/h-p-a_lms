from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render # noqa

from core import utils # noqa

from teachers.forms import TeacherCreateForm
from teachers.models import Teacher

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "first_name": fields.Str(
        required=False,
    ),
    "last_name": fields.Str(
        required=False,
    ),
    "age": fields.Int(
        required=False,
    )
},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    for param_name, param_value in args.items():
        if param_value:
            teachers = teachers.filter(**{param_name: param_value})

    records = utils.format_records(teachers)

    html_form = """
    <body>
    <form action="" method="get">
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="first_name" ><br><br>
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="last_name" ><br><br>
        <label>Age:</label>
        <input type="number" name="age"><br><br>
        <input type="submit" value="Submit">
    </form>
    </body>
    """

    return HttpResponse(html_form + records)


@csrf_exempt
def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    html_form = f"""
    <body>
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Submit">
    </form>
    </body>
    """

    return HttpResponse(html_form)
