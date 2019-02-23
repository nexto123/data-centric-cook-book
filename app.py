import os
from flask import Flask, render_template ,redirect, request, url_for, flash,session,  Blueprint
from flask_pymongo import PyMongo, pymongo
from flask_paginate import Pagination, get_page_args, current_app


app = Flask(__name__)
app.secret_key = 'Ernesto_papa'
app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = "mongodb://admin:dimension123@ds125574.mlab.com:25574/cook_book"

class ProductionConfig():
    SESSION_COOKIE_NAME = 'session name'
    SESSION_PERMANENT = True

mongo = PyMongo(app)

@app.route('/')
@app.route("/home", methods=['POST','GET'])
def home():
    recipes = mongo.db.recipes.find()
    return render_template('index.html',recipes=recipes)

# this route displays recipes in the database
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
    categories = mongo.db.categories.find())
    
# accepts requests from add recipe page and inserts recipes into db
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        