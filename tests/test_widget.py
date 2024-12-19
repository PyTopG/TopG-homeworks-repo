import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def unidentified_string() -> tuple:
    return (
        "Maestro 1596837868705199",
        "Счет 73654108430135874305",
        "Visa Classic 6831982476737658",
        "Счет 35383033474447895560",
    )


@pytest.mark.parametrize(
    "unidentified_string, " "expected",
    (
        [
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
            ("Счет 35383033474447895560", "Счет **5560"),
        ]
    ),
)
def test_mask_account_card(unidentified_string: str, expected: str) -> None:
    assert mask_account_card(unidentified_string) == expected


def test_mask_account_card_empty_input() -> None:
    with pytest.raises(ValueError):
        mask_account_card("")


def test_mask_account_card_invalid_type() -> None:
    with pytest.raises(TypeError):
        mask_account_card(213515)


@pytest.fixture
def date() -> tuple:
    return "2024-03-11T02:26:18.671407", "2024-05-12T02:26:18.671407"


@pytest.mark.parametrize(
    "date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-05-12T02:26:18.671407", "12.05.2024")]
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected


def test_get_date_empty_date() -> None:
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_date(213425)
