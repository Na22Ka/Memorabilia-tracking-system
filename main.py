from datetime import date

# Функция 1: Определение категории вещи по её типу
def get_category(item_type: str) -> str:
    """Возвращает категорию вещи по её типу."""
    item_type = item_type.lower().strip()

    if item_type == "фотография":
        return "Семейный фотоархив"
    elif item_type == "сувенир":
        return "Сувениры и подарки"
    elif item_type == "реликвия":
        return "Семейные реликвии"
    elif item_type == "монета" or item_type == "марка":
        return "Коллекция"
    else:
        return "Прочее"


# Функция 2: Вычисление возраста вещи
def calculate_age(year: int) -> int:
    """Вычисляет возраст вещи по году её создания/получения."""
    current_year = date.today().year
    return current_year - year


# Функция 3: Определение статуса вещи по возрасту
def get_status(age: int) -> str:
    """Определяет статус вещи в зависимости от её возраста."""
    if age < 0:
        return "Ошибка: год не может быть в будущем"
    elif age < 5:
        return "Современная вещь"
    elif age < 30:
        return "Памятная вещь"
    elif age < 100:
        return "Винтажная вещь"
    else:
        return "Историческая реликвия"

# Функция 4 (бонус): Проверка корректности года
def is_valid_year(year: int) -> bool:
    """Проверяет, что год находится в разумных пределах."""
    current_year = date.today().year
    return 1800 <= year <= current_year

# Основной сценарий
def main():
    print("=" * 50)
    print("   СИСТЕМА УЧЁТА ПАМЯТНЫХ ВЕЩЕЙ")
    print("=" * 50)

    item_name = input("Введите название вещи: ").strip()
    item_type = input("Введите тип (фотография/сувенир/реликвия/монета/марка): ").strip()
    year_input = input("Введите год создания или получения вещи: ").strip()

    # Преобразование типа
    if not year_input.isdigit():
        print("Ошибка: год должен быть целым числом.")
        return

    year = int(year_input)

    # Проверка корректности года
    if not is_valid_year(year):
        print("Ошибка: год вне допустимого диапазона (1800 – текущий год).")
        return

    # Вызовы функций
    category = get_category(item_type)
    age = calculate_age(year)
    status = get_status(age)

    # Вывод результата
    print("\n" + "-" * 50)
    print("   КАРТОЧКА ВЕЩИ")
    print("-" * 50)
    print(f"Название:  {item_name}")
    print(f"Тип:       {item_type}")
    print(f"Категория: {category}")
    print(f"Год:       {year}")
    print(f"Возраст:   {age} лет")
    print(f"Статус:    {status}")
    print("-" * 50)


# Точка входа
if __name__ == "__main__":
    main()