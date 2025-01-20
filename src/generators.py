from typing import Iterator, Optional


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Optional[dict]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции,
    и возвращает первую транзакцию, где валюта равна заданной, или None, если такой транзакции нет."""
    return next(
        (
            transaction
            for transaction in transactions
            if transaction.get("operationAmount").get("currency").get("code") == currency
        ),
        None,
    )


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции,
    и возвращает их описание"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 0, stop: int = 9999999999999999) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    if start < 0 or stop < 0 or start > stop:
        raise ValueError("Параметры start и stop должны быть неотрицательными и start не должен превышать stop.")
    if stop > 9999999999999999:
        raise ValueError("Значение stop не должно превышать 9999999999999999.")
    zero_card_number = "0000000000000000"
    for i in range(start, stop + 1):
        # Форматируем номер карты, добавляя ведущие нули
        new_card_number = str(f"{zero_card_number[:-len(str(i))]}{i}")
        # Возвращаем номер карты в формате XXXX XXXX XXXX XXXX
        yield f"{new_card_number[0:4]} {new_card_number[4:8]} {new_card_number[8:12]} {new_card_number[12:]}"
