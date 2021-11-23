from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
MONGO_URI = os.environ.get('MONGO_URI')
app.config['MONGO_URI']=MONGO_URI+'?authSource=admin'
mongo_client=PyMongo(app)
db=mongo_client.db
@app.route('/')
def home():
    return "Hey Hello World!!!"

@app.route('/add_movie')
def add_movie():
    movie_details={'Name':'The Story of My Life','Director':'Adithya','Producer':'Narayan','IMDB_Rating':9.8}
    db.movie.insert_one(movie_details)
    return "Movie Added Successfully"

@app.route('/get_movies')
def get_movies():
    movie=db.movie.find({})
    return jsonify([todo for todo in movie])


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)