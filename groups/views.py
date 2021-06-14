from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Group

from django.shortcuts import render # noqa

from webargs import fields
from webargs.djangoparser import use_args


@use_args({
    "name": fields.Str(
        required=False,
    ),
    "lessons_count": fields.Int(
        required=False,
    ),
    "lessons_passed": fields.Int(
        required=False,
    )
},
    location="query"
)
def get_groups(request, args):
    groups = Group.objects.all()
    for param_name, param_value in args.items():
        if param_value:
            groups = groups.filter(**{param_name: param_value})

    records = format_records(groups)

    html_form = """
    <body>
    <form action="" method="get">
        <label for="fname">Name:</label>
        <input type="text" id="fname" name="name" ><br><br>
        <label>Start date:</label>
        <input type="date" name="start"><br><br>
        <label>Lessons count:</label>
        <input type="text" name="lessons_count"><br><br>
        <label>Lessons passed:</label>
        <input type="text" name="lessons_passed"><br><br>
        <input type="submit" value="Submit">
    </form>
    </body>
    """

    return HttpResponse(html_form + records)


@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    form = GroupCreateForm()

    html_form = f"""
    <body>
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Submit">
    </form>
    </body>
    """

    return HttpResponse(html_form)


def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(str(elem) for elem in lst)
