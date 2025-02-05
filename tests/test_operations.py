import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.operations import read_financial_operations_csv, read_financial_operations_excel


class TestFinancialOperations(unittest.TestCase):

    @patch(
        "builtins.open", new_callable=mock_open, read_data="date,amount,description\n2023-01-01,100,Test transaction\n"
    )
    def test_read_financial_operations_csv(self, mock_file):
        result = read_financial_operations_csv("dummy_path.csv")
        expected = [{"date": "2023-01-01", "amount": "100", "description": "Test transaction"}]
        self.assertEqual(result, expected)
        mock_file.assert_called_once_with("dummy_path.csv", mode="r", newline="", encoding="utf-8")

    @patch("pandas.read_excel")
    def test_read_financial_operations_excel(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame(
            {"date": ["2023-01-01"], "amount": [100], "description": ["Test transaction"]}
        )
        result = read_financial_operations_excel("dummy_path.xlsx")
        expected = [{"date": "2023-01-01", "amount": 100, "description": "Test transaction"}]
        self.assertEqual(result, expected)
        mock_read_excel.assert_called_once_with("dummy_path.xlsx")
