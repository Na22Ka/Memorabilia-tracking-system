from collections.abc import Iterator


def add_item(
    items: dict[int, dict],
    item_name: str,
    category: str,
    year: int
) -> int:
    
    if not item_name.strip():
        raise ValueError("название вещи не может быть пустым")
    item_id = max(items, default=0) + 1
    items[item_id] = {
        "id": item_id,
        "name": item_name.strip(),
        "category": category.strip(),
        "year": year,
    }
    return item_id


def find_item(items: dict[int, dict], query: str) -> list[dict]:
    found = []
    for item in items.values():
        if query.lower() in item["name"].lower():
            found.append(item)
    return found


def check_item_category(
    items: dict[int, dict],
    item_id: int,
    category: str
) -> bool:
    item = items.get(item_id)
    if item is None:
        return False
    return item["category"].lower() == category.lower()


def filter_items_by_year(
    items: dict[int, dict],
    min_year: int
) -> Iterator[dict]:
    for item in items.values():
        if item["year"] >= min_year:
            yield item


def sort_items(items: dict[int, dict]) -> list[dict]:
    """Вернуть вещи, упорядоченные по году (от старых к новым)."""
    return sorted(items.values(), key=lambda item: item["year"])


def get_statistics(items: dict[int, dict]) -> dict:
    by_category: dict[str, int] = {}
    for item in items.values():
        category = item["category"]
        by_category[category] = by_category.get(category, 0) + 1
    oldest = None
    newest = None
    if items:
        oldest = min(items.values(), key=lambda item: item["year"])
        newest = max(items.values(), key=lambda item: item["year"])
    return {
        "total": len(items),
        "by_category": by_category,
        "oldest": oldest,
        "newest": newest,
    }
