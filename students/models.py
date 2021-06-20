import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from students.validators import adult_validator, email_validator, phone_validator


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False, validators=[
        MinLengthValidator(2)
    ])
    last_name = models.CharField(max_length=80, null=False)
    age = models.IntegerField(default=42)
    email = models.EmailField(max_length=120, null=True, validators=[
        email_validator
    ])
    birthday = models.DateField(default=datetime.date.today, null=True, validators=[
        adult_validator
    ])
    enroll_date = models.DateField(default=datetime.date.today, null=True)
    graduate_date = models.DateField(default=datetime.date.today, null=True)
    phone_number = models.TextField(max_length=16, null=True, unique=True, validators=[
        phone_validator
    ])

    def __str__(self):
        return f'{self.full_name()}, {self.birthday}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def generate_students(count):
        faker = Faker()
        for _ in range(count):
            st = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                phone_number=faker.phone_number()
            )
            st.save()
