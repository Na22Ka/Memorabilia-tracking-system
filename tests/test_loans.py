from datetime import date

import pytest

from loans import cancel_loan, create_loan, is_item_available


def test_is_item_available():
    loans = []
    assert is_item_available(loans, 1, date(2026, 9, 15))


def test_duplicate_loan_forbidden():
    loans = []
    create_loan(loans, 1, date(2026, 9, 15))
    assert not is_item_available(loans, 1, date(2026, 9, 15))


def test_duplicate_loan_raises():
    loans = []
    create_loan(loans, 1, date(2026, 9, 15))
    with pytest.raises(ValueError):
        create_loan(loans, 1, date(2026, 9, 15))


def test_other_date_is_available():
    loans = []
    create_loan(loans, 1, date(2026, 9, 15))
    assert is_item_available(loans, 1, date(2026, 9, 20))


def test_cancel_loan():
    loans = []
    loan = create_loan(loans, 1, date(2026, 9, 15))
    assert cancel_loan(loans, loan["id"])
    assert loans == []
