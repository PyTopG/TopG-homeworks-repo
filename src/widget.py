from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(unidentified_string: str) -> str:
    """Функция,которая используется для маскировки номера карты/счета"""
    if not unidentified_string:
        raise ValueError("Отсутствуют данные")
    if not isinstance(unidentified_string, (str)):
        raise TypeError("Неверный тип данных")
    if "Счет" in unidentified_string:
        return f"Счет {get_mask_account(unidentified_string[5:])}"
    else:
        return f"{unidentified_string[:-16]}{get_mask_card_number(unidentified_string[-16:])}"


def get_date(date: str) -> str:
    """Функция, которая возвращает только дату"""
    if not date:
        raise ValueError("Отсутствует какая-либо информация")
    if not isinstance(date, (str)):
        raise TypeError("Неверный формат ввода данных")
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
