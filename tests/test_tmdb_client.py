from tmdb_client import TMDBClient
from unittest.mock import Mock

def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list