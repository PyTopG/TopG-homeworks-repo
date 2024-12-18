def filter_by_state(incoming_data: list, chosen_state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list_of_dicts = []
    for dictionary in incoming_data:
        if dictionary.get("state") == chosen_state:
            new_list_of_dicts.append(dictionary)
    return new_list_of_dicts


def sort_by_date(incoming_data: list, is_reverse: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате"""
    sorted_list = sorted(incoming_data, key=lambda date: date["date"], reverse=is_reverse)
    return sorted_list
