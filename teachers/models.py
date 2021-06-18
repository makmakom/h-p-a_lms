from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    age = models.IntegerField(default=42)
    subject = models.CharField(max_length=120)
    experience = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.full_name()}, {self.age}, {self.subject}, {self.experience}'

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
                experience=faker.text()
            )
            t.save()
