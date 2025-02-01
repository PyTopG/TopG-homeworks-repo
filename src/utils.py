import json
import os


def load_transactions_from_json(file_path: str) -> list[dict]:
    """Функция, которая принимает на вход json файл со списком словарей о транзакциях
    и возвращает его в виде объекта Python"""
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        print(f"Файл не найден: {file_path}")
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                print("Загруженные данные не являются списком.")
                return []
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return []
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")
        return []


file_path = r"C:\PythonProjects\HomeWork\data\operations.json"
transactions = load_transactions_from_json(file_path)
