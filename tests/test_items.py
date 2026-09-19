import pytest

from items import (
    add_item,
    check_item_category,
    filter_items_by_year,
    find_item,
    get_statistics,
    sort_items,
)


def make_items():
    items = {}
    add_item(items, "Открытка от бабушки", "Письма", 2015)
    add_item(items, "Ракушка из Крыма", "Путешествия", 2018)
    add_item(items, "Медаль за полумарафон", "Спорт", 2022)
    return items


def test_add_item():
    items = {}
    add_item(items, "Открытка от бабушки", "Письма", 2015)
    assert len(items) == 1


def test_add_item_empty_name_raises():
    with pytest.raises(ValueError):
        add_item({}, "   ", "Письма", 2015)


def test_find_item_ignores_case():
    assert find_item(make_items(), "ОТКРЫТКА")


def test_check_item_category():
    assert check_item_category(make_items(), 2, "путешествия")


def test_sort_items_by_year():
    years = [item["year"] for item in sort_items(make_items())]
    assert years == [2015, 2018, 2022]


def test_filter_items_by_year():
    found = list(filter_items_by_year(make_items(), 2018))
    assert len(found) == 2


def test_get_statistics():
    stats = get_statistics(make_items())
    assert stats["total"] == 3
    assert stats["by_category"]["Спорт"] == 1
