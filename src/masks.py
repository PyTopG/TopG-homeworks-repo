def get_mask_card_number(card_num: int | str) -> str:
    """Функция, которая возвращает маску номера карты"""
    if not card_num:
        raise ValueError("Вы ничего не ввели")
    if not isinstance(card_num, (int | str)):
        raise TypeError("Неверный формат ввода данных")
    if len(str(card_num)) != 16:
        raise ValueError("Неверное количество введенных символов")
    return f"{str(card_num)[:4]} {str(card_num)[4:6]}** **** {str(card_num)[-4:]}"


def get_mask_account(account_num: int | str) -> str:
    """Функция, которая возвращает маску номера счета"""
    if not account_num:
        raise ValueError("Вы ничего не ввели")
    if not isinstance(account_num, (int | str)):
        raise TypeError("Неверный формат ввода данных")
    if len(str(account_num)) != 20:
        raise ValueError("Неверное количество введенных символов")
    return f"**{str(account_num)[-4:]}"
