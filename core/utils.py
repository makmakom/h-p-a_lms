def format_records(lst, url_part) -> object:
    if len(lst) == 0:
        return '(Emtpy recordset)'
    result = []
    for elem in lst:
        formatted = f'<a href="/{url_part}/update/{elem.id}">{elem.id}</a> {elem}'
        result.append(formatted)
    return '<br>'.join(result)
