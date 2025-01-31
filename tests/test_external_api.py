import unittest
from unittest.mock import patch, Mock
from dotenv import load_dotenv

# Измените путь импорта в зависимости от вашей структуры каталогов
from src.external_api import convert_to_rub

class TestCurrencyConversion(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'RUB': 75.0}}
        mock_response.status_code = 200
        mock_get.return_value = mock_response


    @patch('src.external_api.requests.get')
    def test_convert_to_rub_currency_already_rub(self, mock_get):
        transaction = {'amount': 100, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch('src.external_api.requests.get')
    def test_convert_to_rub_api_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("API Error")
        mock_get.return_value = mock_response


    @patch('src.external_api.requests.get')
    def test_convert_to_rub_invalid_currency(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {}}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'INVALID'}
        result = convert_to_rub(transaction)
        self.assertIsNone(result)

if __name__ == '__main__':
    load_dotenv()
    unittest.main()
