import json
from pathlib import Path


def _read_json(filename: str) -> list[dict]:
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден, данные начнутся с нуля.")
        return []
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён, данные начнутся с нуля.")
        return []
    if not isinstance(data, list):
        print(f"Файл {filename} имеет неверный формат.")
        return []
    return data


def _write_json(filename: str, data: list[dict]) -> None:
    try:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Не удалось сохранить файл {filename}: {error}")


def load_items(filename: str) -> dict[int, dict]:
    items = {}
    for item in _read_json(filename):
        try:
            items[item["id"]] = item
        except (KeyError, TypeError):
            print("Пропущена некорректная запись о вещи.")
    return items


def save_items(filename: str, items: dict[int, dict]) -> None:
    _write_json(filename, list(items.values()))


def load_loans(filename: str) -> list[dict]:
    return _read_json(filename)


def save_loans(filename: str, loans: list[dict]) -> None:
    _write_json(filename, loans)
