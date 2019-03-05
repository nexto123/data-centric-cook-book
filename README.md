# Data-Centric Project

A Code Institute Project. Data-Centric.

## Getting Started

Ingrido is the shortening of ingredients a suitable name i found for my cook-book project. It is simply the showcasing of food recipes that can be easily accessed. First log in and gain full access. 

## UX

 Since the Question specified an online cookbook, it's imperative we stay as close as we can within the scope of what has been prescribed, at least in design. For the design, I'm going to be using grids of 3squares per row, with a total of 6 squares per page. The materialise cards can do a good job with that. The cards will have 3 sections; being 1. the card-image, 2. card-title, and 3.crud-section.
 The card-image has 2 sections, the actual image which will bear the recipe image and on the flipped side where I'll put my recipe ingredients. So if a user should click on the image of a card it will flip and the ingredients will be displayed. The card title is where some details like recipe author, country of origin of the recipe, and the name of recipe entries will be placed.  
 And finally the crud section. This section will basically contain some crud buttons. Examples are the edit and delete buttons, which when clicked will send the user to the appropriate page or take the required action.
 
 
 
## Prerequisites

To get started let's make some preps. You'd need to have a basic understanding of the flask framework and at least a grasp on some frontend technologies. Besides the usual CSS and HTML, it would be handy to know a bit of bootstrap or materialise.css. In our case, we will be using materialise.css for the front-end. 


And for the backend I'll usually start by setting up the environment for my flask app by entering in my cli tool

``` 
$ [sudo]pip install virtualenv 
```
Virtual env is a tool that serves as a sandbox for your python projects. So, what this does is, it tricks your computer into looking for and installing packages in your project directory rather than in your python directory. 
But unfortunately, we won't be working from it with this project.

Within the <head> tags place your title and various <links> to connect to your HTML. The bootstrap4 CSS or whatever cdn to be used will be placed in the head tags. It's important to place the script tags at the bottom of the page but right before the closing body tags.
To connect the CSS files flask has a twist from the usual, it follows this structure;
 
```
 <link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}" type="text/css" media="screen,projection" />
 ```
 
 It's important to state that the layout or base file should contain the static structure. We can extend the header and footer to the rest of the templates along with other needed functionalities placed within the base file. 
 

## Used Extensions for App

[Flask](http://flask.pocoo.org/) - render_template ,redirect, request, url_for, flash, session, Blueprint

[Flask-Paginate](https://pythonhosted.org/Flask-paginate/)- Pagination, get_page_args, current_app

[Pymomgo](https://api.mongodb.com/python/current/)- PyMongo, pymongo


## Database setup

For my database am using MongoDB looped by the flask extension called Pymongo.
The database is hosted by MongoDB's [Mlab](mlab.com). 
Mongo db is a very popular database, classified as a non relation database. 
It is basically an unstructured database, in common terms, one can say it dumps the data without much order.
To set up a database on mlab, it will require registration 

The document panel which becomes where your entries are set up must be in a JSON-like format.
```
{
"name": "Ernest"
}
```
After setup, MongoDB will generate a link for you, and this link will go into your flask app.
```
mongodb://<dbuser>:<dbpassword>@ds163103.mlab.com:63103/mytestdb
```
Now you will place your link inside the flask app.py.
Voila! Your database is ready.


## Testing

Usually, python apps are required to use test automation, and the python unittest libraries can be employed for the job.
But at this time all my test were done manually.

i. The Like button: In the normal sense, a validated user can only like a post once, but since my goal is to demonstrate a basic interaction of the database and not to overstep the scope of the project, user validation wasn't my aim for the like button. I simply developed a counting system to keep track of clicks and save the value to the database. So when the user clicks the favourite button, it would be counted as +1. I also gave all the entries a like value of 1 just as not left bare. I could start them with zero or empty space that wasn't my goal.

ii. Flask-Paginate: The paging function wasn't very efficient as the application grew cumbersome and difficult due to poor documentation of flask-paginate. In the future, I'll employ the use of ``` request. referrer ```
URL style for my pages, as I've come to under its use better.

iii. The recipe ingredient: The placement wasn't the most ideal, and my plan was to have all the necessary features on the card. Some ingredients could be a lot in terms of wording and would be best if there was an allotted page for every recipe. In the future, I will add a read more button to give an extension to the recipe on a full page.

At this point, the app works well on the various mobile screens, the iphone6/6+/7/7+/8/8+, Galaxy s5 and desktops. 


## Deployment To Git & Heroku

After committing to git with the appropriate messages, 
I'll now perform a git push to my GitHub Repo.
To create a new repository;
* first assign a repository name on GitHub since that's what I'm using.
* write a short description of the site to be uploaded.
* You will either select to initialize your repository with a README.md file. (optional)
* create your repository.
* You will perform a git remote login
* And finally, git push -u origin master.

Heroku is a cloud platform that lets you build, deliver, monitor and scale apps.
To deploy to Heroku, there are two critical steps to perform even before your final commit message.
We have the Procfile and the requirement.txt files. 
These are critical necessities if you are deploying to Heroku.
To get requirement.txt file input this into your cli.
```
sudo pip3 freeze —local > requirements.txt
```
To get the Procfile file input this into your cli.
```
$ echo web: python app.py > Procfile
```




* ```heroku login ```- if you've created an account, you'll need to provide the email.
* ```heroku git:clone -a cook-book123 ```
* ``` cd cook-book123 ```
* ``` git push heroku master ```

#### [Live Version](https://ingrido.herokuapp.com/)

### Features to be added:

1. user profile page.
2. limit on crud access> user can only delete what they contributed'
3. Extension page to the full recipe details.
4. Social Media Extensions 


### Features:

1. Home page > Log in to activate crud functionality on the cards.
* Add a recipe by clicking on the big '+' sign.
* click on the image to have access to ingredients.
2. Category page > You can add and delete categories
* Click on a meal type to sort out and display the number of items with that category in the database.




## Versioning

 Git


## Author

Ernest Bruce Brown


## Media

* Google Images


## Acknowledgments

* Chris. Z



