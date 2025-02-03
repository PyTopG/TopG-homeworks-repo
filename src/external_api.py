import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
headers = {"apikey": f"{api_key}"}


def convert_to_rub(transaction: dict) -> float:
    """Функция для получения суммы операции в рублях"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()  # Проверка на ошибки HTTP

        # Получаем данные из ответа
        result = response.json()

        # Проверяем, есть ли нужные данные
        if "result" in result:
            return round(result["result"], 2)  # Возвращаем сумму в рублях
        else:
            print("Ошибка: данные не содержат 'result'")
            return None
    except requests.exceptions.RequestException:
        return None  # Обработка ошибок API
    except KeyError:
        return None  # Обработка отсутствующих ключей
