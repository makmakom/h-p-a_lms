from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=80, null=False)
    age = models.IntegerField(default=42)
    subject = models.CharField(max_length=120)
    experience = models.TextField(max_length=500)
