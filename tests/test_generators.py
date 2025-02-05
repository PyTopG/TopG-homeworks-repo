import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура, которая предоставляет тестовые данные
@pytest.fixture
def transactions():
    return [
        {
            "id": 93971950,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00.000000",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
    ]


def test_filter_by_currency(transactions):
    txs = transactions
    test_cases = {"USD": 123456789, "RUB": 93971950, "EUR": 142264268, "JPY": None}

    for currency, expected_id in test_cases.items():
        result = list(filter_by_currency(txs, currency=currency))
        if expected_id is None:
            assert len(result) == 0
        else:
            assert len(result) == 1
            assert result[0]["id"] == expected_id

    result = list(filter_by_currency(txs))
    assert len(result) == 1
    assert result[0]["id"] == 123456789


@pytest.fixture
def transactions_descriptions(transactions):
    return transaction_descriptions(transactions)


def test_transactions_descriptions(transactions_descriptions):
    assert next(transactions_descriptions) == "Перевод организации"
    assert next(transactions_descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_empty():
    # Тестируем случай с пустым списком транзакций
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            0,
            5,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999,
            10001,
            [
                "0000 0000 0000 9999",
                "0000 0000 0001 0000",
                "0000 0000 0001 0001",
            ],
        ),
        (
            0,
            0,
            [
                "0000 0000 0000 0000",
            ],
        ),
    ],
)
def test_card_number_generator_normal(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


# Параметризованный тест для проверки исключений
@pytest.mark.parametrize(
    "start, stop, expected_message",
    [
        (5, 3, "start не должен превышать stop"),
        (-1, 5, "Параметры start и stop должны быть неотрицательными"),
        (0, -5, "Параметры start и stop должны быть неотрицательными"),
        (0, 10000000000000000, "Значение stop не должно превышать 9999999999999999"),
    ],
)
def test_card_number_generator_exceptions(start, stop, expected_message):
    with pytest.raises(ValueError, match=expected_message):
        list(card_number_generator(start, stop))
