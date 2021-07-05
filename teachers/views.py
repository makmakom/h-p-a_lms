from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from teachers.forms import TeacherCreateForm, TeacherUpdateForm, TeachersFilter
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
},
    location="query"
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    for param_name, param_value in args.items():
        teachers = teachers.filter(**{param_name: param_value})

    obj_filter = TeachersFilter(data=request.GET, queryset=teachers)

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'obj_filter': obj_filter,
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
    teacher = Teacher.objects.get(id=pk)

    if request.method == 'GET':
        form = TeacherUpdateForm(instance=teacher)
    elif request.method == 'POST':
        form = TeacherUpdateForm(
            data=request.POST,
            instance=teacher
        )
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/update.html',
        context={
            'form': form,
            'title': 'Update teacher',
        }
    )


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/delete.html',
        context={
            'teacher': teacher,
            'title': 'Delete teacher',
        }
    )
