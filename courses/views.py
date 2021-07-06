from courses.forms import CourseCreateForm, CourseFilter, CourseUpdateForm
from courses.models import Course

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def get_courses(request):
    groups = Course.objects.all()
    obj_filter = CourseFilter(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'obj_filter': obj_filter,
            'title': 'Courses List'
        }
    )


def create_course(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))
    else:
        form = CourseCreateForm()

    return render(
        request=request,
        template_name='courses/create.html',
        context={
            'form': form,
            'title': 'Create course'
        }
    )


def update_course(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'GET':
        form = CourseUpdateForm(instance=course)
    elif request.method == 'POST':
        form = CourseUpdateForm(
            data=request.POST,
            instance=course
        )
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/update.html',
        context={
            'form': form,
            'title': 'Update course',
        }
    )


def delete_course(request, pk):
    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(
        request=request,
        template_name='courses/delete.html',
        context={
            'course': course,
            'title': 'Delete course',
        }
    )
