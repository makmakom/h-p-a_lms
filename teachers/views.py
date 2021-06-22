from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core import utils  # noqa

from teachers.forms import TeacherCreateForm, TeacherUpdateForm

from teachers.models import Teacher

from webargs import fields, validate
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

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'teachers': teachers,
            'title': 'Teachers List'
        }
    )


def create_teacher(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={
            'form': form,
            'title': 'Create teacher'
        }
    )


def update_teacher(request, pk):
    group = Teacher.objects.get(id=pk)

    if request.method == 'GET':
        form = TeacherUpdateForm(instance=group)
    elif request.method == 'POST':
        form = TeacherUpdateForm(
            data=request.POST,
            instance=group
        )
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    html_form = f"""
    <body>
    <form method="post">
      {form.as_p()}
      <input type="submit" value="Save">
    </form>
    </body>
    """

    return HttpResponse(html_form)
