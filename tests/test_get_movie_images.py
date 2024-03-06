import unittest
from unittest.mock import Mock
import tmdb

class TestGetMovieImages(unittest.TestCase):
    
    def test_get_movie_images(self):
        # Ustawienie odpowiedniego mocka dla funkcji call_tmdb_api
        tmdb.call_tmdb_api = Mock(return_value={
            'backdrops': [{'file_path': 'url1'}, {'file_path': 'url2'}],
            'posters': [{'file_path': 'url3'}, {'file_path': 'url4'}]
        })

        # Oczekiwane dane wynikowe
        expected_result = {
            'backdrops': ['url1', 'url2'],
            'posters': ['url3', 'url4']
        }

        # Wywołanie funkcji i sprawdzenie wyniku
        result = tmdb.get_movie_images(123)

        # Przetworzenie wyniku mocka na oczekiwany format
        processed_result = {
            'backdrops': [image['file_path'] for image in result['backdrops']],
            'posters': [image['file_path'] for image in result['posters']]
        }

        self.assertEqual(processed_result, expected_result)

if __name__ == '__main__':
    unittest.main()