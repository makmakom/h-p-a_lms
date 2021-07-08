from django.db import models

from faker import Faker


class Course(models.Model):
    name = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def generate_courses(count):
        faker = Faker()
        for _ in range(count):
            gr = Course(
                name=faker.job(),
            )
            gr.save()
