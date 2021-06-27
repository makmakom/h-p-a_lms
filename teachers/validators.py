from django.core.exceptions import ValidationError

import teachers.models


def phone_validator(phone):
    if teachers.models.Teacher.objects.filter(phone_number=phone).exists():
        raise ValidationError('Phone exists')
