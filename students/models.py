import datetime

from core.models import Person

from django.db import models

from groups.models import Group


class Student(Person):
    enroll_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students', blank=True)

    def __str__(self):
        return f'{self.full_name()}, {self.birthday}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def _generate(cls):
        super()._generate()
