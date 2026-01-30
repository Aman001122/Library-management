from datetime import date

FINE_PER_DAY = 2

def calculate_fine(due_date):
    late_days = (date.today() - due_date).days
    return late_days * FINE_PER_DAY if late_days > 0 else 0
