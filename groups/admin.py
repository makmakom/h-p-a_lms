from django.contrib import admin

from students.models import Student

from .models import Group


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
