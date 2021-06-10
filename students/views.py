from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm
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

    records = format_records(students)

    html_form = """
    <form action="" method="get">
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="first_name" ><br><br>
        
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="last_name" ><br><br>
        
        <label>Age:</label>
        <input type="number" name="age"><br><br>
        
        <input type="submit" value="Submit">
    </form>
    """

    return HttpResponse(html_form + records)


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/students/')

    form = StudentCreateForm()

    html_form = f"""
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Submit">
    </form>
    """

    return HttpResponse(html_form)


def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(str(elem) for elem in lst)
