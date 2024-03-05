    
import requests

class TMDBClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api.themoviedb.org/3/"

    def call_api(self, endpoint):
        full_url = self.base_url + endpoint
        headers = {"Authorization": f"Bearer {self.api_token}"}
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()

    def get_popular_movies(self, list_type="popular"):
        return self.call_api(f"movie/{list_type}")

    def get_single_movie(self, movie_id):
        return self.call_api(f"movie/{movie_id}")

    def get_single_movie_cast(self, movie_id):
        return self.call_api(f"movie/{movie_id}/credits")

    def get_movies_list(self, list_type):
        return self.call_api(f"movie/{list_type}")


def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

# Example usage:
if __name__ == "__main__":
    API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZGI3ZWVkMWEyMDYyNmE3OTkzZGU3NDVjNjAyMTFjZiIsInN1YiI6IjY1Nzc2ZTM4NGJmYTU0MDBmZTdmNTcyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XVEouCriGjxEOpKzsLMbcsmVUa6DT8AgHd_Hvpojurk"

    tmdb_client = TMDBClient(API_TOKEN)

    popular_movies = tmdb_client.get_popular_movies()
    print("Popular movies:", popular_movies)

    movie_id = 550  # Example movie ID
    single_movie = tmdb_client.get_single_movie(movie_id)
    print("Single movie:", single_movie)

    single_movie_cast = tmdb_client.get_single_movie_cast(movie_id)
    print("Single movie cast:", single_movie_cast)

    movies_list = tmdb_client.get_movies_list("top_rated")
    print("Top rated movies list:", movies_list)

