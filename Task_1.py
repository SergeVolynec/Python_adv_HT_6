"""В модуль с проверкой даты добавьте возможность запуска в терминале
 с передачей даты на проверку."""

from datetime import datetime as dt
from calendar import isleap
from sys import argv


def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return print("Это дата")
    except:
        return print("Это не дата")


def _isleap(year: int):
    print("Год високосный" if isleap(year) else "Год не високосный")


if __name__ == '__main__':
    if len(argv) > 1:
        print(argv)
        check_date(argv[1])
