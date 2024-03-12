from flask import Flask, render_template, request
from tmdb import get_poster_url
import tmdb

app = Flask(__name__)


@app.route('/movies_catalogue')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    movies = tmdb.get_movies_list(selected_list)["results"]
    return render_template("homepage.html", movies=movies, current_list=selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(poster_path, size="w342"):
        return get_poster_url(poster_path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movies_catalogue/<int:movie_id>")
def movie_details(movie_id):
    details = tmdb.get_single_movie(movie_id)
    cast = tmdb.get_single_movie_cast(movie_id)["cast"]
    return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)


