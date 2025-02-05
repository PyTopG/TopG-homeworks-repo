import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from main import load_transactions_from_csv, load_transactions_from_excel, load_transactions_from_json


class TestMain(unittest.TestCase):
    def test_load_transactions_from_json(self):
        mock_data = (
            '[{"description": "Открытие вклада", "amount": "40542 руб.", '
            '"status": "EXECUTED", "date": "08.12.2019", "account": "4321"}]'
        )
        with patch("builtins.open", mock_open(read_data=mock_data)):
            transactions = load_transactions_from_json("dummy_path.json")
            self.assertEqual(len(transactions), 1)
            self.assertEqual(transactions[0]["description"], "Открытие вклада")

    def test_load_transactions_from_csv(self):
        mock_data = "description,amount,status,date,account\nОткрытие вклада,40542 руб.,EXECUTED,08.12.2019,4321\n"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            transactions = load_transactions_from_csv("dummy_path.csv")
            self.assertEqual(len(transactions), 1)
            self.assertEqual(transactions[0]["description"], "Открытие вклада")

    def test_load_transactions_from_excel(self):
        mock_data = pd.DataFrame(
            {
                "description": ["Открытие вклада"],
                "amount": ["40542 руб."],
                "status": ["EXECUTED"],
                "date": ["08.12.2019"],
                "account": ["4321"],
            }
        )

        with patch("pandas.read_excel", return_value=mock_data):
            transactions = load_transactions_from_excel("dummy_path.xlsx")
            self.assertEqual(len(transactions), 1)
            self.assertEqual(transactions[0]["description"], "Открытие вклада")

    @patch("builtins.input", side_effect=["1", "dummy_path.json", "executed", "да", "по возрастанию", "да"])
    @patch("builtins.print")
    def test_main_function(self, mock_print, mock_input):
        # Здесь мы можем протестировать логику main()
        with patch(
            "builtins.open",
            mock_open(
                read_data='[{"description": "Открытие вклада", "amount": "40542 руб.", '
                '"status": "EXECUTED", "date": "08.12.2019", "account": "4321"}]'
            ),
        ):
            from main import main

            main()

            # Проверяем, что print был вызван с ожидаемыми параметрами
            mock_print.assert_any_call("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
            mock_print.assert_any_call('Операции отфильтрованы по статусу "EXECUTED".')
            mock_print.assert_any_call('Операции отфильтрованы по статусу "EXECUTED".')


if __name__ == "__main__":
    unittest.main()
