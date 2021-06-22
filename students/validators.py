from datetime import datetime

from django.core.exceptions import ValidationError

import students.models


def adult_validator(birthday, adult_age_limit=18):
    age = datetime.now().year - birthday.year
    if age < adult_age_limit:
        raise ValidationError(f'Age should bee grater then {adult_age_limit} y.o.')


def phone_validator(phone):
    if students.models.Student.objects.filter(phone_number=phone).exists():
        raise ValidationError('Phone exists')


def email_validator(email):
    pass


class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, birthdate):
        adult_validator(birthdate)
        