import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename=r"C:\PythonProjects\HomeWork\logs\masks.log",  # Запись логов в файл
    filemode="w",
)


def get_mask_card_number(card_num: int | str) -> str:
    """Функция, которая возвращает маску номера карты"""
    logger.debug(f"Получение маски номера карты: {card_num}")

    if not card_num:
        logger.error("Ошибка: Вы ничего не ввели")
        raise ValueError("Вы ничего не ввели")

    if not isinstance(card_num, (int, str)):
        logger.error("Ошибка: Неверный формат ввода данных")
        raise TypeError("Неверный формат ввода данных")

    if len(str(card_num)) != 16:
        logger.error("Ошибка: Неверное количество введенных символов")
        raise ValueError("Неверное количество введенных символов")

    masked_card = f"{str(card_num)[:4]} {str(card_num)[4:6]}** **** {str(card_num)[-4:]}"
    logger.info(f"Сгенерированная маска номера карты: {masked_card}")
    return masked_card


def get_mask_account(account_num: int | str) -> str:
    """Функция, которая возвращает маску номера счета"""
    logger.debug(f"Получение маски номера счета: {account_num}")

    if not account_num:
        logger.error("Ошибка: Вы ничего не ввели")
        raise ValueError("Вы ничего не ввели")

    if not isinstance(account_num, (int, str)):
        logger.error("Ошибка: Неверный формат ввода данных")
        raise TypeError("Неверный формат ввода данных")

    if len(str(account_num)) != 20:
        logger.error("Ошибка: Неверное количество введенных символов")
        raise ValueError("Неверное количество введенных символов")

    masked_account = f"**{str(account_num)[-4:]}"
    logger.info(f"Сгенерированная маска номера счета: {masked_account}")
    return masked_account
