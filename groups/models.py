from django.db import models

from faker import Faker


class Group(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(max_length=500, default='No description', null=False)
    start = models.DateField()
    lessons_count = models.IntegerField(default=12, null=False)
    lessons_passed = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def generate_groups(count):
        faker = Faker()
        for _ in range(count):
            count = faker.random_int(8, 41, 4)
            gr = Group(
                name=faker.job(),
                description=faker.text(),
                start=faker.date_time_this_decade(),
                lessons_count=count,
                lessons_passed=faker.random_int(0, count + 1)
            )
            gr.save()
