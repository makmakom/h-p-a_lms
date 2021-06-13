from datetime import datetime

from django.core.exceptions import ValidationError


def adult_validator(birthday):
    ADULT_AGE_LIMIT = 18

    age = datetime.now().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should bee grater then 18 y.o.')
