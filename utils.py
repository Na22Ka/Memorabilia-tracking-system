from datetime import date, datetime


def input_int(prompt: str) -> int:
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date(prompt: str) -> date:
    while True:
        raw_value = input(prompt).strip()
        try:
            return datetime.strptime(raw_value, "%d.%m.%Y").date()
        except ValueError:
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ.")
