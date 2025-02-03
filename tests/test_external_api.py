import unittest
from unittest.mock import Mock, patch

import requests

from src.external_api import convert_to_rub


class TestConvertToRub(unittest.TestCase):

    @patch("requests.request")
    def test_convert_to_rub_success(self, mock_request):
        # Настройка имитации успешного ответа от API
        mock_response = Mock()
        mock_response.json.return_value = {"result": 100.0}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        transaction = {"operationAmount": {"amount": 10, "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)
        mock_request.assert_called_once()

    @patch("requests.request")
    def test_convert_to_rub_no_result(self, mock_request):
        # Настройка имитации ответа без 'result'
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        transaction = {"operationAmount": {"amount": 10, "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        self.assertIsNone(result)
        mock_request.assert_called_once()

    @patch("requests.request")
    def test_convert_to_rub_request_exception(self, mock_request):
        # Настройка имитации исключения при запросе
        mock_request.side_effect = requests.exceptions.RequestException

        transaction = {"operationAmount": {"amount": 10, "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        self.assertIsNone(result)
        mock_request.assert_called_once()

    @patch("requests.request")
    def test_convert_to_rub_key_error(self, mock_request):
        # Настройка имитации успешного ответа, но с отсутствующим ключом
        mock_response = Mock()
        mock_response.json.return_value = {"unexpected_key": 100.0}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        transaction = {"operationAmount": {"amount": 10, "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        self.assertIsNone(result)
        mock_request.assert_called_once()
