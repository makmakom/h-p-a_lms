from faker import Faker


def format_records(lst, url_part) -> str:
    if len(lst) == 0:
        return '(Emtpy recordset)'
    result = []
    for elem in lst:
        formatted = f'<a href="/{url_part}/update/{elem.id}">{elem.id}</a> {elem}'
        result.append(formatted)
    return '<br>'.join(result)


def fake_phone_number(fake: Faker) -> str:
    return f'+380{fake.msisdn()[4:]}'
