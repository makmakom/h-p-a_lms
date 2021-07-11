from django.contrib import admin

from .models import Group
from students.models import Student


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'last_name',
        'first_name',
        'email',
        'age',
    ]

    # readonly_fields = fields
    # show_change_link = True             # edit in Student model

    extra = 0               # default = 3


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        # 'start_date',
        # 'end_date',
        'headman',
        # 'days_of_week',
    ]

    fields = [
        'name',
        # ('start_date', 'end_date', 'days_of_week'),
        'headman',
        'teachers',
    ]

    inlines = [StudentsInlineTable]


admin.site.register(Group, GroupAdmin)