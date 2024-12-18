from typing import Union


def get_mask_card_number(card_num: Union[int]) -> Union[str]:
    """Функция, которая возвращает маску номера карты"""
    return f"{str(card_num)[:4]} {str(card_num)[4:6]}** **** {str(card_num)[-4:]}"


def get_mask_account(account_num: Union[int]) -> Union[str]:
    """Функция, которая возвращает маску номера счета"""
    return f"**{str(account_num)[-4:]}"
