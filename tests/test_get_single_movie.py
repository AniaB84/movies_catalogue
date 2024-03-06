import tmdb
from unittest.mock import Mock

def test_get_single_movie(monkeypatch):
   # Dane symulowanej odpowiedzi z serwera
   mock_single_movie = {'title': 'Movie 1'}

   # Tworzymy obiekt Mock dla requests.get i ustawiamy go jako zwracany obiekt
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie

   # Ustawiamy mock za pomocą monkeypatch 
   monkeypatch.setattr("tmdb.requests.get", requests_mock)

   # Wywołujemy funkcję, którą testujemy
   single_movie = tmdb.get_single_movie(movie_id={})

   # Sprawdzamy, czy otrzymane dane są zgodne z oczekiwanymi
   assert single_movie == mock_single_movie
   
if __name__ == "__main__":
    test_get_single_movie()