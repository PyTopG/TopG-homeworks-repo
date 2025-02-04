import csv

import pandas as pd


def read_financial_operations_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV файла и возвращает список словарей."""
    transactions = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


def read_financial_operations_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel файла и возвращает список словарей."""
    transactions = pd.read_excel(file_path)
    return transactions.to_dict(orient="records")
