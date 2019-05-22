import os
from flask import Flask, render_template ,redirect, request, url_for, flash, session, Blueprint
from flask_paginate import Pagination, get_page_args, current_app
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config.from_pyfile('app.cfg')
app.secret_key = 'Ernesto_papa'
app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = "mongodb://admin:dimension123@ds125574.mlab.com:25574/cook_book"


class ProductionConfig():
    SESSION_COOKIE_NAME = 'session name'
    SESSION_PERMANENT = True
    

mongo = PyMongo(app)
mod = Blueprint('recipes', __name__)


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
    return render_template('index.html', recipes = recipes, pagination = pagination, page=page)

    
@app.route('/likes/<page>/<recipe_id>')
def likes(recipe_id, page):
    new_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    figure = int(new_recipe['likes'])
    like_recipe = mongo.db.recipes
    #this will increase the value of like when clicked
    like_recipe.update({"_id":ObjectId(recipe_id)},
        {"$inc":
            {
            "likes": 1
             }
        },upsert=False, multi=False)
        #page number is bn parsed into the url as a variable 
    return redirect('/home?page={}'.format(page))


# this route displays recipes in the database
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
    categories = mongo.db.categories.find())
    
    

# accepts requests from add recipe page and inserts recipes into db
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    category_name= request.form['category_name']
    recipe_author= request.form['recipe_author']
    recipe_name =request.form['recipe_name']
    country_of_origin= request.form['country_of_origin']
    recipe_ingredients= request.form['recipe_ingredients']
    likes= int(request.form['likes'])
    photo_url= request.form['photo_url']
    recipes = mongo.db.recipes
    recipes.insert_one({'recipe_author':recipe_author, 
    'recipe_name':recipe_name, 
    'recipe_ingredients':recipe_ingredients,
    'country_of_origin':country_of_origin, 
    'likes':likes, 'photo_url':photo_url, 'category_name':category_name})
    return redirect(url_for('home'))
    
    
# this route edits recipes and is sent to the update route    
@app.route('/edit_recipe/<recipe_id>/<page>')
def edit_recipe(page, recipe_id):
    new_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', new_recipe = new_recipe, 
    categories=categories, page=page)
    
    
# this routes updates the recipes from the edit route
@app.route('/update_recipe/<recipe_id>', methods=['POST','GET'])
def update_recipe(recipe_id):
    page = request.form.get('page')
    print(page)
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form['category_name'],
        'recipe_author':request.form['recipe_author'],
        'recipe_name':request.form['recipe_name'],
        'recipe_ingredients': request.form['recipe_ingredients'],
        'photo_url': request.form['photo_url'],
        'country_of_origin': request.form['country_of_origin'],
        'likes': int(request.form['likes'])
    })
    return redirect('/home?page={}'.format(page))
    
    
    
# this route deletes the recipe     
@app.route('/delete_recipe/<page>/<recipe_id>')
def delete_recipe(page, recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect('/home?page={}'.format(page))  
        
# category page
@app.route('/add_categories')
def add_category():
    return render_template('add_categories.html')

#this route displays categories in the database
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories = mongo.db.categories.find())
    
 #this route inserts categories   
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category = mongo.db.categories
    cat_insert = {'category_name': request.form['category_name']}
    category.insert_one(cat_insert)
    return redirect(url_for('get_categories'))
    
#this route edits categories     
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))    

#this routes deletes categories
@app.route('/delete_categories/<category_id>')
def delete_categories(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))   

# search route for categories
@app.route('/list_recipes/<category_name>')
def list_recipes(category_name):
    
    #Pagination
    page = request.args.get(get_page_args, type=int, default=1)
    page, per_page,offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    search = False
    q = request.args.get('q')
    if q:
        search = True
    # using the skip and limit curser and per_page setted as 10 items perpage      
    
    recipes = mongo.db.recipes.find({"category_name":category_name})
    pagination = Pagination( page=page, per_page=per_page,total=recipes.count(), search=search, record_name='recipes',offset=offset)
    #pagination is parsed into the template to be displayed
    return render_template('list_recipes.html',recipes=recipes, page=page, pagination=pagination )
        
    
#login page route
@app.route('/login')
def login_page():
    return render_template('login_page.html')
    

#Logging out of session after use.
@app.route('/session_loggout')
def session_logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
