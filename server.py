from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import crud
from jinja2 import StrictUndefined


CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "eat-this"

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage."""
    return render_template("homepage.html", recipes=crud.get_most_faved())


@app.route("/all_recipes")
def all_recipes():
    """View all recipes."""
    recipes = crud.get_recipes()
    return render_template("all_recipes.html", recipes=recipes)

@app.route("/login_page")
def display_login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""
    login_email = request.form.get("email")
    login_password = request.form.get("password")
    #import pdb; pdb.set_trace()
    if crud.get_user_by_email(login_email):

        user = crud.get_user_by_email(login_email)
        if login_password != user.password:
            flash("Incorrect password. Try again")
        else:
            #add the user's user_id to the flask session
            session['current_user'] = user.user_id
            session['current_email'] = user.email
            #session['current_user_obj'] = user
            flash(f'Logged in as {user.email}')
    else:
        flash("Looks like we don't know you yet! ")
        return redirect("/registration")
    return redirect("/")

@app.route('/logout')
def logout_user():
    """ Log user out, delete their info from the session """

    session['current_user'] = None
    session['current_email'] = None
   # session['current_user_obj'] = None

    flash("You have logged out. Goodbye!")
    return redirect('/')


@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/registration')
def display_registarion_page():
    return render_template("user_registration.html")
    
@app.route('/user_registration', methods=["POST"])
def register_user():
    """create an account"""
    #assign email and password variables with request.form.get
    email = request.form.get("email")
    password = request.form.get("password")
    username = request.form.get("username")
    full_name = request.form.get("full_name")
    if crud.get_user_by_email(email):
        flash("This user already exists, please, log in")    
    else:
        new_user = crud.create_user(email, password, username), full_name
        db.session.add(new_user)
        db.session.commit()
        flash(f"Welcome, {username}!")
    return redirect('/')


@app.route('/new_recipe')
def display_add_new_recipe():
    return render_template("add_new_recipe.html")


@app.route('/add_new_recipe', methods=["POST"])
def add_new_recipe():
    """create an account"""
    #assign email and password variables with request.form.get
    title = request.form.get("title")
    cuisine = request.form.get("cuisine")
    diet = request.form.get("diet")
    new_recipe = crud.create_recipe(title=title, cuisine=cuisine, added_by=session['current_user'], 
    diet=diet)
    db.session.add(new_recipe)
    db.session.commit()
    new_recipe_id = new_recipe.recipe_id
    #new_recipe_id = crud.get_last_recipe_by_added(session['current_user']).recipe_id

    image = request.files['recipe_img']
    result = cloudinary.uploader.upload(image, api_key=CLOUDINARY_KEY,
        api_secret=CLOUDINARY_SECRET,
        cloud_name=CLOUD_NAME)
    url = result['secure_url']
    new_image = crud.create_image(url,recipe_id=new_recipe_id)
    db.session.add(new_image)
    db.session.commit()
    '''
    here will be the file handling something,
    then create img for the recipe and steps
    image = create_image(url,recipe_id=None)
    '''  
    return redirect(f'/recipe/{new_recipe_id}')
    #return render_template("recipe.html")

@app.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    return render_template("recipe.html", recipe=crud.get_recipe_by_id(recipe_id))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
