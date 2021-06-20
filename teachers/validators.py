from django.core.exceptions import ObjectDoesNotExist, ValidationError

import teachers.models


def phone_validator(phone):
    try:
        teachers.models.Teacher.objects.get(phone_number=phone)
    except ObjectDoesNotExist:
        return True

    raise ValidationError('Phone exists')
