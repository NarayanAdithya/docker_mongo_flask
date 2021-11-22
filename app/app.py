from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
MONGO_URI = os.environ.get('MONGO_URI')
db=PyMongo(app,uri=MONGO_URI)

@app.route('/')
def home():
    return "Hey Hello World"


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)