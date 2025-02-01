import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
headers = {"apikey": f"{api_key}"}


def convert_to_rub(transaction: dict) -> float:
    """Функция для получения суммы операции"""

    def get_exchange_rate(currency: str) -> any:
        """Функция для получения курса валюты к рублю"""
        payload = {}
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()
            return data["rates"]["RUB"]
        except Exception as e:
            print(f"Ошибка при получении курса валют: {e}")
            return None

    currency = transaction["currency"]
    amount = transaction["amount"]

    if currency == "RUB":
        return float(amount)  # Если уже в рублях, просто возвращаем сумму

    # Получаем курс валюты к рублю
    exchange_rate = get_exchange_rate(currency)

    if exchange_rate is None:
        print("Не удалось получить курс валюты.")
        return None

    # Конвертируем сумму в рубли
    return float(amount) * exchange_rate
