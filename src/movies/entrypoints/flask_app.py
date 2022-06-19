from email.policy import default
from pickle import FALSE
from flask import Flask, request
from movies import models
import psycopg2
import json

import movie_fetcher
import movies.dbPost as dbPost
import movies.dbFetch as dbFetch
import movies.prefKey as prefKey
import csvRead
import entries

app = Flask(__name__)
models.start_mappers()

# Basic Hello World
@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

# Update movie csv file
@app.route("/update", methods=["GET"])
def disp_movies():
    movie_fetcher.main()

    return "Called movie fetcher, csv now up to date", 200

# /Register user in database given proper usar data
@app.route("/register", methods=["POST"])
def add_user():
    # Request args
    username = request.args.get('username')
    password = request.args.get('password')
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    p3 = request.args.get('p3')

    # Call in algorithm for key calculation
    preference_key = prefKey.calc_value(p1,p2,p3)
    res = dbPost.add_user(username,password,preference_key)
    return res, 200

# /Recommend a list of movies for a user given proper parameters
@app.route("/recommend", methods=["GET"])
def get_rec():
    # Request args
    username = request.args.get('username') 
    # Ask for kind of object to be searched. Default value "Movie". Can be expanded into more values
    typeOf = request.args.get('typeOf', "Movie") 
    sizeOf = request.args.get('sizeOf', 10)
    # Ratings defaults to True, returns arr in desc order. Changing to 0 will return values in desc.
    ratings = request.args.get('ratings', 1)

    ##CHAIN OF RESPONSABILITY
    user = dbFetch.dbUser(username)

    # Validate de existence of a user
    if user.valid == -1 :
        return "USER DOES NOT EXIST", 200

    # Query user preference key from database.
    preference_key = user.fetch_user_key()

    # Reac CSV and recover recomendations based on preference key and ratings
    listaEntries = csvRead.read_csv_movies(ratings,preference_key,sizeOf)
    
    # Create list of objects
    ##Solid 3 LSP: by making an entry an object we can change only the type of object we want
    entry = entries.EntriesMaker()
    payload = entry.makeJson(listaEntries,typeOf)
    
    # return listaEntries[0][1], 200
    return  payload,200
