import datetime

from django.db import models


# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    age = models.IntegerField(default=42)
    email = models.EmailField(max_length=120, null=True)
    birthday = models.DateField(default=datetime.date.today, null=True)

    def __str__(self):
        return f'{self.full_name()}, {self.birthday}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
