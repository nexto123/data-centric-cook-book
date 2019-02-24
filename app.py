import os
from flask import Flask, render_template ,redirect, request, url_for, flash,session, Blueprint
from flask_paginate import Pagination, get_page_args, current_app
from flask_pymongo import PyMongo, pymongo
from multiprocessing import Value
from bson.objectid import ObjectId

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
    #login system
    username = request.form.get('username')
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        if username == None or username == '':
            flash('Please enter a username', 'error')
            return redirect(url_for('login_page'))
        else:
            flash('Welcome {}'.format(username),'success')
            return redirect(url_for('home'))
            
            
    #Pagination
    page = request.args.get(get_page_args, type=int, default=1)
    page, per_page,offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    search = False
    q = request.args.get('q')
    if q:
        search = True
    # using the skip and limit curser and per_page setted as 10 items perpage      
    recipes = mongo.db.recipes.find().sort('_id', pymongo.DESCENDING).limit(per_page).skip((page - 1) * per_page)
 
    pagination = Pagination( page=page, per_page=per_page,total=recipes.count(), search=search, record_name='recipes',offset=offset)
    #pagination is parsed into the template to be displayed
    return render_template('index.html', recipes = recipes, pagination = pagination)


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



# this route edits recipes and is sent to the update route    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    new_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', new_recipe = new_recipe, 
    categories=categories)
    







if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        