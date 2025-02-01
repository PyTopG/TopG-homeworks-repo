import unittest
from unittest.mock import patch, mock_open

# Предположим, что ваша функция load_transactions_from_json находится в файле my_module.py
from src.utils import load_transactions_from_json


class TestLoadTransactionsFromJson(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"operationAmount": {"currency": {"name": "USD"}}}]')
    @patch('os.path.isfile')
    def test_load_transactions_success(self, mock_isfile, mock_open):
        # Настройка mock для проверки существования файла
        mock_isfile.return_value = True

        file_path = 'dummy_path.json'
        transactions = load_transactions_from_json(file_path)

        self.assertEqual(len(transactions), 1)  # Ожидаем, что загружен один элемент
        self.assertEqual(transactions[0]['operationAmount']['currency']['name'], 'USD')

    @patch('os.path.isfile')
    def test_load_transactions_file_not_found(self, mock_isfile):
        # Настройка mock для случая, когда файл не существует
        mock_isfile.return_value = False

        file_path = 'dummy_path.json'
        transactions = load_transactions_from_json(file_path)

        self.assertEqual(transactions, [])  # Ожидаем, что вернется пустой список

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.isfile')
    def test_load_transactions_invalid_json(self, mock_isfile, mock_open):
        # Настройка mock для проверки существования файла
        mock_isfile.return_value = True
        mock_open.side_effect = IOError("File not accessible")  # Эмулируем IOError

        file_path = 'dummy_path.json'
        transactions = load_transactions_from_json(file_path)

        self.assertEqual(transactions, [])  # Ожидаем, что вернется пустой список

    @patch('builtins.open', new_callable=mock_open, read_data='{"not": "a list"}')
    @patch('os.path.isfile')
    def test_load_transactions_not_a_list(self, mock_isfile, mock_open):
        # Настройка mock для проверки существования файла
        mock_isfile.return_value = True

        file_path = 'dummy_path.json'
        transactions = load_transactions_from_json(file_path)

        self.assertEqual(transactions, [])  # Ожидаем, что вернется пустой список
