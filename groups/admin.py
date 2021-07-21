from django.contrib import admin

from .models import Group
from students.models import Student


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'last_name',
        'first_name',
        'email',
        'birthdate',
        'age',
    ]
    readonly_fields = ['age']
    show_change_link = True
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start',
        'headman',
    ]
    fields = [
        'name',
        'course',
        'headman',
        'teachers',
    ]
    inlines = [StudentsInlineTable]
    search_fields = [
        'name',
        'start',
    ]


admin.site.register(Group, GroupAdmin)
