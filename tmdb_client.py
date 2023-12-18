import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZGI3ZWVkMWEyMDYyNmE3OTkzZGU3NDVjNjAyMTFjZiIsInN1YiI6IjY1Nzc2ZTM4NGJmYTU0MDBmZTdmNTcyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XVEouCriGjxEOpKzsLMbcsmVUa6DT8AgHd_Hvpojurk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

get_popular_movies()

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:8]

how_many = []
get_movies(how_many)


def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

poster_path = []
get_poster_url(poster_path)






