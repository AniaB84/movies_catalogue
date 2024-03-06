import tmdb
from unittest.mock import Mock

def test_get_single_movie_cast(monkeypatch):
    # Dane symulowanej odpowiedzi z serwera
   mock_single_movie_cast = {'cast': [{'name': 'Actor 1'}, {'name': 'Actor 2'}]}

   # Tworzymy obiekt Mock dla requests.get i ustawiamy go jako zwracany obiekt
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast

    # Ustawiamy mock za pomocą monkeypatch
   monkeypatch.setattr("tmdb.requests.get", requests_mock)

    # Wywołujemy funkcję, którą testujemy
   single_movie_cast = tmdb.get_single_movie_cast(movie_id=123)

    # Sprawdzamy, czy otrzymane dane są zgodne z oczekiwanymi
   assert single_movie_cast == mock_single_movie_cast

if __name__ == "__main__":
    test_get_single_movie_cast()
    