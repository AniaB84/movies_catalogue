import pytest, unittest
from unittest.mock import Mock
from main import app

@pytest.mark.parametrize("list_type", ['movie/popular', 'movie/top_rated', 'movie/now_playing', 'movie/upcoming'])
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("main.homepage", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(list_type)

if __name__ == '__main__':
    unittest.main()
