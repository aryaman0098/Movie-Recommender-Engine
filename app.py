import requests
from flask import Flask, render_template, request
from flask.wrappers import Response 
import pandas as pd
import pickle
from tmdbv3api import TMDb, Movie
import json


tmdb = TMDb()
tmdbMovie = Movie()
tmdb.api_key = "62520f0cb1e77a57e1c66e073f288bf6"

movieSimilarity = pickle.load(open("movieSimilarity.pkl", "rb"))
data = pd.read_csv("processedData/FinalData.csv")


def fetchPosterOverView(movieID):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}".format(movieID, tmdb.api_key))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data["poster_path"], data["overview"]


def fetchInputDetails(movieId):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}&append_to_response=credits".format(movieId, tmdb.api_key)) 
    data = response.json()
    details = {}
    details["title"] = data["original_title"]
    details["releaseDate"] = data["release_date"]
    details["overview"] = data["overview"]
    details["actors"] = []
    for i in range(0, 10):
        details["actors"].append(data["credits"]["cast"][i]["original_name"])
    return details


def recommend(movie):
    movieIndex = data[data["Title"] == movie].index[0]
    distances = movieSimilarity[movieIndex]
    similarMoviesList = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[0:13]
    
    listOfRecommendations = []
    recommendedMoviesPosters = []
    inputMovieDetails = []
    recommendedMoviesOverview = []
    path = ""
    overview = ""
    for i in similarMoviesList:
        listOfRecommendations.append(data.iloc[i[0]].Title)
        movieId = tmdbMovie.search(data.iloc[i[0]].Title)[0].id
        if movie == data.iloc[i[0]].Title:
            inputMovieDetails = fetchInputDetails(movieId)
        path, overview= fetchPosterOverView(movieId)
        recommendedMoviesPosters.append(path)
        recommendedMoviesOverview.append(overview)
    return listOfRecommendations, recommendedMoviesPosters, inputMovieDetails, recommendedMoviesOverview



app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    requestMethod = request.method
    movieList = []

    for i in data["Title"]:
        movieList.append(i)

    print(len(movieList))
    print(movieSimilarity.shape)


    recommendedMovies = []
    recommendedMoviesPosters = []
    inputDetails = []
    overview = []
    x = False
    if request.method == "POST":
        try:
            recommendedMovies, recommendedMoviesPosters, inputDetails, overview = recommend(request.form["InputMovie"])
            x = True
        except:
            recommendedMovies = ["Movies Not Found!!"]
    return render_template("home.html", names = recommendedMovies, 
                                        posters = recommendedMoviesPosters, 
                                        details = inputDetails,
                                        overview = overview, 
                                        movieList = movieList,
                                        toPrint = x)

if __name__ == "__main__":
    app.run()