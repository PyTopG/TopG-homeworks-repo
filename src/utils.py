import json
import logging
import os

# Настройка логирования
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    filename=r"C:\PythonProjects\HomeWork\logs\utils.log",  # Запись логов в файл
    filemode="w",
)


def load_transactions_from_json(file_path: str) -> list[dict]:
    """Функция, которая принимает на вход json файл со списком словарей о транзакциях
    и возвращает его в виде объекта Python"""
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Данные успешно загружены из файла.")
                return data
            else:
                logger.warning("Загруженные данные не являются списком.")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
        return []
    except IOError as e:
        logger.error(f"Ошибка ввода-вывода: {e}")
        return []


file_path = r"C:\PythonProjects\HomeWork\data\operations.json"
transactions = load_transactions_from_json(file_path)

# Дополнительный лог для отображения загруженных транзакций
if transactions:
    logger.info(f"Загружено {len(transactions)} транзакций.")
else:
    logger.info("Нет загруженных транзакций.")
