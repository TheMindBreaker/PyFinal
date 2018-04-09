def dia():
    import time
    return time.strftime("%d/%m/%Y")
    return time.strftime("%d/%m/%Y")

def primer_dia():
    import datetime
    return datetime.date.isoformat(datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().isoweekday() % 7))

def ultimo_dia():
    import datetime
    return datetime.date.isoformat(datetime.datetime.now() + datetime.timedelta(days=datetime.datetime.now().isoweekday() % 7))
