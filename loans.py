from datetime import date


def is_item_available(
    loans: list[dict],
    item_id: int,
    loan_date: date
) -> bool:
    date_str = loan_date.isoformat()
    for loan in loans:
        same_item = loan["item_id"] == item_id
        same_date = loan["loan_date"] == date_str
        if same_item and same_date:
            return False
    return True


def create_loan(
    loans: list[dict],
    item_id: int,
    loan_date: date
) -> dict:
    if not is_item_available(loans, item_id, loan_date):
        raise ValueError("вещь на эту дату уже выдана")
    loan_id = max((loan["id"] for loan in loans), default=0) + 1
    loan = {
        "id": loan_id,
        "item_id": item_id,
        "loan_date": loan_date.isoformat(),
    }
    loans.append(loan)
    return loan


def cancel_loan(loans: list[dict], loan_id: int) -> bool:
    for index, loan in enumerate(loans):
        if loan["id"] == loan_id:
            loans.pop(index)
            return True
    return False


def get_loan_status(is_available: bool) -> str:
    """Вернуть текстовый статус вещи."""
    if is_available:
        return "Вещь доступна для выдачи"
    return "Вещь уже выдана"
