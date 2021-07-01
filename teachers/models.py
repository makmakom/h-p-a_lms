from core.models import Person
from core.utils import fake_phone_number

from django.db import models

from faker import Faker

from groups.models import Group

from teachers.validators import phone_validator


class Teacher(Person):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    age = models.IntegerField(default=42)
    subject = models.CharField(max_length=120)
    experience = models.TextField(max_length=500)
    phone_number = models.TextField(max_length=16, null=True, unique=True, validators=[
        phone_validator
    ])
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='teachers')

    def __str__(self):
        return f'{self.full_name()}, {self.age}, {self.subject}, {self.experience}, {self.group}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def generate_teachers(count):
        faker = Faker()
        for _ in range(count):
            t = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=faker.random_int(25, 45),
                subject=faker.job(),
                experience=faker.text(),
                phone_number=fake_phone_number(faker)
            )
            t.save()

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(1000, 3000)
        obj.save()