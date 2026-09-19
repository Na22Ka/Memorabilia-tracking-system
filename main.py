from collections.abc import Iterable
from datetime import date
from pathlib import Path

from items import (
    add_item,
    check_item_category,
    filter_items_by_year,
    find_item,
    get_statistics,
    sort_items,
)
from loans import (
    cancel_loan,
    create_loan,
    get_loan_status,
    is_item_available,
)
from storage import load_items, load_loans, save_items, save_loans
from utils import input_date, input_int

BASE_DIR = Path(__file__).resolve().parent
ITEMS_FILE = str(BASE_DIR / "data" / "items.json")
LOANS_FILE = str(BASE_DIR / "data" / "loans.json")

MENU = """
=== Система учета памятных вещей ===
1. Показать вещи
2. Найти вещь по названию
3. Добавить вещь
4. Проверить категорию вещи
5. Проверить доступность на дату
6. Оформить выдачу
7. Отменить выдачу
8. Показать выдачи
9. Показать вещи по годам (сортировка)
10. Показать вещи не ранее года
11. Статистика
0. Выход"""


def show_items(items: Iterable[dict]) -> None:
    rows = list(items)
    if not rows:
        print("Ничего не найдено.")
        return
    print(f"{'ID':<4}{'Название':<32}{'Категория':<16}{'Год':<6}")
    for item in rows:
        print(
            f"{item['id']:<4}{item['name']:<32}"
            f"{item['category']:<16}{item['year']:<6}"
        )


def show_loans(loans: list[dict], items: dict[int, dict]) -> None:
    if not loans:
        print("Выдач нет.")
        return
    for loan in loans:
        item = items.get(loan["item_id"])
        name = item["name"] if item else "неизвестная вещь"
        loan_date = date.fromisoformat(loan["loan_date"])
        print(f"№{loan['id']}: {name} — {loan_date:%d.%m.%Y}")


def show_statistics(items: dict[int, dict]) -> None:
    stats = get_statistics(items)
    print(f"Всего вещей: {stats['total']}")
    for category, count in stats["by_category"].items():
        print(f"  {category}: {count}")
    if stats["oldest"]:
        print(f"Самая старая: {stats['oldest']['name']} "
              f"({stats['oldest']['year']})")
        print(f"Самая новая: {stats['newest']['name']} "
              f"({stats['newest']['year']})")


def add_item_dialog(items: dict[int, dict]) -> None:
    name = input("Название вещи: ")
    category = input("Категория: ")
    year = input_int("Год: ")
    try:
        item_id = add_item(items, name, category, year)
    except ValueError as error:
        print(f"Ошибка: {error}")
    else:
        print(f"Вещь добавлена, ID = {item_id}")


def check_category_dialog(items: dict[int, dict]) -> None:
    item_id = input_int("ID вещи: ")
    category = input("Категория: ")
    if check_item_category(items, item_id, category):
        print("Да, вещь относится к этой категории")
    else:
        print("Нет, либо вещь не найдена")


def check_availability_dialog(
    items: dict[int, dict],
    loans: list[dict]
) -> None:
    item_id = input_int("ID вещи: ")
    if item_id not in items:
        print("Вещь с таким ID не найдена.")
        return
    loan_date = input_date("Дата (ДД.ММ.ГГГГ): ")
    print(get_loan_status(is_item_available(loans, item_id, loan_date)))


def create_loan_dialog(items: dict[int, dict], loans: list[dict]) -> None:
    item_id = input_int("ID вещи: ")
    if item_id not in items:
        print("Вещь с таким ID не найдена.")
        return
    loan_date = input_date("Дата выдачи (ДД.ММ.ГГГГ): ")
    try:
        loan = create_loan(loans, item_id, loan_date)
    except ValueError as error:
        print(f"Ошибка: {error}")
    else:
        print(f"Выдача оформлена, №{loan['id']}")


def cancel_loan_dialog(loans: list[dict]) -> None:
    loan_id = input_int("Номер выдачи: ")
    if cancel_loan(loans, loan_id):
        print("Выдача отменена")
    else:
        print("Выдача с таким номером не найдена")


def main() -> None:
    items = load_items(ITEMS_FILE)
    loans = load_loans(LOANS_FILE)
    while True:
        print(MENU)
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_items(items.values())
        elif choice == "2":
            show_items(find_item(items, input("Часть названия: ")))
        elif choice == "3":
            add_item_dialog(items)
            save_items(ITEMS_FILE, items)
        elif choice == "4":
            check_category_dialog(items)
        elif choice == "5":
            check_availability_dialog(items, loans)
        elif choice == "6":
            create_loan_dialog(items, loans)
            save_loans(LOANS_FILE, loans)
        elif choice == "7":
            cancel_loan_dialog(loans)
            save_loans(LOANS_FILE, loans)
        elif choice == "8":
            show_loans(loans, items)
        elif choice == "9":
            show_items(sort_items(items))
        elif choice == "10":
            min_year = input_int("Год: ")
            show_items(filter_items_by_year(items, min_year))
        elif choice == "11":
            show_statistics(items)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестный пункт меню, попробуйте ещё раз.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nРабота программы прервана.")
