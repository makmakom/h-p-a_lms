import datetime

from dateutil.relativedelta import relativedelta
from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=50)
    age = models.IntegerField(default=42)
    email = models.EmailField(max_length=120, null=True)
    birthdate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}'

    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthdate).years
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        faker = Faker()
        st = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            birthdate=faker.date_between(start_date='-65y', end_date='-18y'),
        )

        st.age = relativedelta(datetime.date.today(), st.birthdate).years
        st.save()
        return st

    @classmethod
    def generate(cls, count):
        for _ in range(count):
            cls._generate()