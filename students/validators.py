from datetime import datetime

from django.core.exceptions import ValidationError, ObjectDoesNotExist

import students.models


def adult_validator(birthday):
    ADULT_AGE_LIMIT = 18

    age = datetime.now().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should bee grater then 18 y.o.')


def phone_validator(phone):
    try:
        students.models.Student.objects.get(phone_number=phone)
    except ObjectDoesNotExist:
        return True

    raise ValidationError('Phone exists')


def email_validator(email):
    if email:
        raise ValidationError('Email error')
