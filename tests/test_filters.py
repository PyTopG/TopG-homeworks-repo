import unittest

from src.filters import count_transactions_by_category, filter_transactions_by_description


class TestFilters(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {
                "description": "Открытие вклада",
                "amount": "40542 руб.",
                "status": "EXECUTED",
                "date": "08.12.2019",
                "account": "4321",
            },
            {
                "description": "Перевод с карты на карту",
                "amount": "130 USD",
                "status": "CANCELED",
                "date": "12.11.2019",
                "account": "3727",
            },
            {
                "description": "Перевод организации",
                "amount": "8390 руб.",
                "status": "EXECUTED",
                "date": "18.07.2018",
                "account": "7202",
            },
            {
                "description": "Перевод со счета на счет",
                "amount": "8200 EUR",
                "status": "PENDING",
                "date": "03.06.2018",
                "account": "0034",
            },
        ]

    def test_filter_transactions_by_description(self):
        result = filter_transactions_by_description(self.transactions, "вклада")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["description"], "Открытие вклада")

        result = filter_transactions_by_description(self.transactions, "перевод")
        self.assertEqual(len(result), 3)

        result = filter_transactions_by_description(self.transactions, "не существующее слово")
        self.assertEqual(len(result), 0)

    def test_count_transactions_by_category(self):
        categories = ["вклад", "перевод"]
        result = count_transactions_by_category(self.transactions, categories)
        self.assertEqual(result["вклад"], 1)
        self.assertEqual(result["перевод"], 3)

        categories = ["перевод", "не существующая категория"]
        result = count_transactions_by_category(self.transactions, categories)
        self.assertEqual(result["перевод"], 3)
        self.assertEqual(result["не существующая категория"], 0)


if __name__ == "__main__":
    unittest.main()
