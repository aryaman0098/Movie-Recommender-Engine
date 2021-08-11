# Movie Recommender Engine

This is a simple Movie Recommender Engine that uses Content Based  recommendation to similar movies on the basis of the input movie by the user. It uses the genres, overview of the movies, actors and the director of the input movie to recommend similar movies. Under the hood, the code first converts the movies into vectors using Term Frequency Inverse Document Frquency (TFIDF) and then uses cosine similarity to find most similar movies with the input movie. Additionally the app uses [Flask](https://flask.palletsprojects.com/en/2.0.x/) to manage its backend and make API calls.

This web app is deployed at : https://movie-recommendations-engine.herokuapp.com

### Dataset

The dataset used for this project is the _[TMDB5000](https://www.kaggle.com/tmdb/tmdb-movie-metadata)_ dataset. Additionally some web scrapping has been done to find the lastest movies.

### Note

Movies upto 2019 have been added in this project. More movies will be added soon.

---

## Instructions to use

To run using this web app, create a virtual env and install the dependencies as mentioned in requirement.txt. To install the dependencies, open command propmt or terminal and run the following command - 

```
pip install -r requirements.txt
```
followed by

```
python app.py
```
Open [localhost:5000](http://127.0.0.1:5000/) in the browser

---
## License

This project is distributed under [MIT license](https://opensource.org/licenses/MIT). Any feedback, suggestions are higly appreciated.











