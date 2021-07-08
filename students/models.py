import datetime

from core.models import Person

from django.db import models

from groups.models import Group


class Student(Person):
    enroll_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate(cls):
        super()._generate()
