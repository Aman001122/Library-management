from datetime import date

FINE_PER_DAY = 2

def calculate_fine(due_date):
    today = date.today()
    late_days = (today - due_date).days
    if late_days > 0:
        return late_days * FINE_PER_DAY
    return 0
