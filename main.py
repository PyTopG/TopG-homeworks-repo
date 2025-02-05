import csv
import json

import pandas as pd


def load_transactions_from_json(file_path: str) -> list:
    """Загружает транзакции из JSON файла."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_transactions_from_csv(file_path: str) -> list:
    """Загружает транзакции из CSV файла."""
    transactions = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


def load_transactions_from_excel(file_path: str) -> list:
    """Загружает транзакции из Excel файла."""
    transactions = pd.read_excel(file_path)
    return transactions.to_dict(orient="records")


def main():
    """функция, которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    file_path = input("Введите путь к файлу: ")

    if choice == "1":
        transactions = load_transactions_from_json(file_path)
    elif choice == "2":
        transactions = load_transactions_from_csv(file_path)
    elif choice == "3":
        transactions = load_transactions_from_excel(file_path)
    else:
        print("Неверный выбор.")
        return

    status = ""
    while status.lower() not in ["executed", "canceled", "pending"]:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ")
        if status.lower() not in ["executed", "canceled", "pending"]:
            print(f'Статус операции "{status}" недоступен.')

    print(f'Операции отфильтрованы по статусу "{status.upper()}".')
    filtered_transactions = [t for t in transactions if t.get("status", "").lower() == status.lower()]

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        filtered_transactions.sort(key=lambda x: x["date"], reverse=(order == "по убыванию"))

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_filter == "да":
        filtered_transactions = [t for t in filtered_transactions if "руб" in t.get("amount", "")]
        return filtered_transactions


if __name__ == "__main__":
    main()
