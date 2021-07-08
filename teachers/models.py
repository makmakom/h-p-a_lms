from random import randint

from core.models import Person

from django.db import models

from groups.models import Group


class Teacher(Person):
    salary = models.PositiveIntegerField(default=1500, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, related_name='teachers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(1000, 3000)
        obj.save()
