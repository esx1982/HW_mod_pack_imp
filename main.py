from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime as dt
from rus2latin_date import Converter

date = dt.now()
c = Converter()

if __name__ == "__main__":
    get_employees(f'Евгений, {date.date()} в {date.time().replace(microsecond=0)}')
    calculate_salary('Евгений', 'менеджер')
    get_employees(f'Maksim, {c.conv(str(date.date()))} в {date.time().replace(microsecond=0)}')
    calculate_salary('Maksim', 'general manager')
    print(c.conv(f"{date.date()}"))