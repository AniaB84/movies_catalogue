import unittest
from unittest.mock import patch, MagicMock
from tmdb import call_tmdb_api
from requests.exceptions import HTTPError


class TestCallTmdbApi(unittest.TestCase):

    @patch('tmdb.requests.get')
    def test_call_tmdb_api(self, mock_get):
        # Ustawienie mocka dla obiektu odpowiedzi HTTP
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"example_key": "example_value"}
        mock_get.return_value = mock_response

         # Dane potrzebne do wykonania żądania HTTP
        API_TOKEN = ""
        endpoint = "example_endpoint"
        expected_url = f"https://api.themoviedb.org/3/{endpoint}"
        expected_headers = {
            "Authorization": f"Bearer {API_TOKEN}"
        }
        # Wywołanie funkcji testowanej
        result = call_tmdb_api(endpoint)

        # Sprawdzenie czy funkcja wykonuje żądanie HTTP poprawnie
        mock_get.assert_called_once_with(expected_url, headers=expected_headers)

        # Sprawdzenie czy zwrócona treść jest zgodna z oczekiwaniami
        self.assertEqual(result, {"example_key": "example_value"})

         # Sprawdzenie czy raise_for_status() zostało wywołane na obiekcie odpowiedzi
        mock_response.raise_for_status.assert_called_once()

    @patch('tmdb.requests.get')
    def test_call_tmdb_api_error(self, mock_get):
        # Ustawienie mocka dla obiektu odpowiedzi HTTP z kodem 404
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Wywołanie funkcji testowanej z adresem końcowym, który spowoduje błąd HTTP
        endpoint = "example_endpoint"
        with self.assertRaises(HTTPError):
            call_tmdb_api(endpoint)

        # Sprawdzenie czy raise_for_status() zostało wywołane na obiekcie odpowiedzi
        mock_response.raise_for_status.assert_called_once()

if __name__ == '__main__':
    unittest.main()
    