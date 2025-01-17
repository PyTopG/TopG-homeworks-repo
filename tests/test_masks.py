import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_num() -> tuple:
    return 1234567891011123, "2345678910111213"


@pytest.mark.parametrize(
    "card_num, expected", ([(1234567891011123, "1234 56** **** 1123"), ("2345678910111213", "2345 67** **** 1213")])
)
def test_get_mask_card_number(card_num: int | str, expected: str) -> None:
    assert get_mask_card_number(card_num) == expected


def test_get_mask_card_number_invalid_length() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(3123425)


def test_get_mask_card_number_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_card_number(["123124", "Lol,kek,cheburek"])


def test_get_mask_card_number_empty_input() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(False)


@pytest.fixture
def account_num() -> tuple:
    return 73654108430135874305, "64686473678894779589"


@pytest.mark.parametrize(
    "account_num, expected", ([(73654108430135874305, "**4305"), ("64686473678894779589", "**9589")])
)
def test_get_mask_account_number(account_num: str | int, expected: str) -> None:
    assert get_mask_account(account_num) == expected


def test_get_mask_account_number_invalid_length() -> None:
    with pytest.raises(ValueError):
        get_mask_account(3123425)


def test_get_mask_account_number_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_account(["erfewf"])


def test_get_maskaccount_number_empty_input() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")
