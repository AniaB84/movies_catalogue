import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZGI3ZWVkMWEyMDYyNmE3OTkzZGU3NDVjNjAyMTFjZiIsInN1YiI6IjY1Nzc2ZTM4NGJmYTU0MDBmZTdmNTcyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XVEouCriGjxEOpKzsLMbcsmVUa6DT8AgHd_Hvpojurk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many=8, list_type="popular"):
    data = get_popular_movies()
    return data["results"][:how_many]


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZGI3ZWVkMWEyMDYyNmE3OTkzZGU3NDVjNjAyMTFjZiIsInN1YiI6IjY1Nzc2ZTM4NGJmYTU0MDBmZTdmNTcyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XVEouCriGjxEOpKzsLMbcsmVUa6DT8AgHd_Hvpojurk"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:8]



def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()







