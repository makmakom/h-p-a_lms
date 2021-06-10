from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=120, null=False)
    start = models.DateField()
    lessons_count = models.IntegerField(default=12, null=False)
    lessons_passed = models.IntegerField(default=0, null=False)
