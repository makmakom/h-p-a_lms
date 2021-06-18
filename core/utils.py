def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(str(elem) for elem in lst)
