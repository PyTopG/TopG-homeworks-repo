def mask_account_card(card_info: str) -> str:
    """Функция,которая используется для маскировки номера карты/счета"""
    if "Счет" in card_info:
        return f"Счет **{str(card_info)[-4:]}"
    else:
        for card_info_element in card_info.split():
            masked_card_number = ""
            if card_info_element.isdigit():
                masked_card_number += (
                    f"{str(card_info_element)[:4]} {str(card_info_element)[5:7]}** **** {str(card_info_element)[-4:]}"
                )
        return card_info.replace(card_info_element, masked_card_number)


def get_date(date_info: str) -> str:
    """Функция,которая возвращает только дату"""
    return f"{date_info[8:10]}.{date_info[5:7]}.{date_info[:4]}"
