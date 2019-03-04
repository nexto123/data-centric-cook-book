# Data-Centric Project

A Code Institute Project. Data-Centric.

## Getting Started
To get started lets make some preps. You'd need to have a basic understanding of the flask framework and and atleast a grasp on some frontend technologies. Besides the usual css and html, it would be handy to know a bit of bootstrap or materialise.css. In our case we will be using materialise.css. 

 Since the project specified an online cook-book it's imperative we stay as close as we can within the scope of what has been prescribed. For the design i'm going to be using grids of 3squares per row, with a total of 6 items per page. The materialise cards can do a good job with that. The cards will have 3 sections; being 1. the card-imge, 2. card-title, and 3.crud-section.
 The card-iamge has 2 sections, on the flipped otherside is where i'll put my recipe ingredients. So if a user should click on the image of a card it flips and the ingredients will be diplayed. The card title,  is where some details like recipe author, country of origin of the recipe, and recipe name entries will placed.  
 And finally the crud section. This section will basically contain some crud buttons. Examples are the edit and delete buttons.
 
 
 
## Prerequisites

I'll ussually start by setting up the environment for my flask app by entering in my cli tool ''' $ [sudo]pip install virtualenv ''' .
Within the <head> tag place your title and various <links> to connect to your HTML. The bootstrap4 CSS cdn to be used will be placed in the head tags as well. It's important to place the script tags at the bottom of the page but right before the closing body tags.
 


i used the page variable from flask paginate to redirect urls back to the pages the came from. 

to create my like button i utilized the $inc pymongo trick to get my counts and left as is.
to not over complicate my project i will stick to my increment feature only. 

To have access to crude activity users will have to add a user name to login. The edit and delete buttons will be deactivated 



since the scope of the project laid very little emphasies on front-end i have 
limited my screen tests to iphone6/6+/7/7+/8/8+,Galaxy s5 and desktops.
