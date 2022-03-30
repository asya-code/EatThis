from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, User, Recipe, Step, Favorite, Ingredient, Image
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
    return render_template("recipes.html", recipes=recipes)

@app.route("/user_recipes")
def user_recipes():
    """View user's recipes."""
    user_id = session['current_user']
    recipes = crud.get_recipes_by_added(user_id)
    username = crud.get_user_by_id(user_id).username
    return render_template("user_recipes.html", recipes=recipes, username=username)

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
    new_recipe= crud.create_recipe(title="new_recipe", added_by=session['current_user'])
    db.session.add(new_recipe)
    db.session.commit()
    return render_template("add_new_recipe.html", recipe_id=new_recipe.recipe_id)


@app.route('/add_new_recipe', methods=["POST"])
def add_new_recipe():
    """new recipe is generated when the page loads,
    this recipe's id will be fetched from the page,
    recipe's attributes will be updated with user's input from current page"""
    updated_recipe_id = request.form.get('recipe_id')
    new_title = request.form.get("title")
    new_cuisine = request.form.get("cuisine")
    new_diet = request.form.get("diet")
    updated_recipe = crud.get_recipe_by_id(updated_recipe_id)
    updated_recipe.title = new_title
    updated_recipe.cuisine = new_cuisine
    updated_recipe.diet = new_diet
    if request.files['recipe_img']:
        image = request.files['recipe_img']
        result = cloudinary.uploader.upload(image, api_key=CLOUDINARY_KEY,
            api_secret=CLOUDINARY_SECRET,
            cloud_name=CLOUD_NAME)
        url = result['secure_url']
        new_image = crud.create_image(url,recipe_id=updated_recipe_id)
        db.session.add(new_image)
    db.session.commit()
    
    return redirect(f'/recipe/{updated_recipe_id}')

@app.route('/recipes/<recipe_id>')
def show_recipe(recipe_id):
    return render_template("recipe.html", recipe=crud.get_recipe_by_id(recipe_id))

@app.route('/add_instr', methods=["POST"])
def add_step():
    instr_text = request.json.get('instructionText')
    order = int(request.json.get('order'))
    recipe_id = int(request.json.get('recipe_id'))
    new_instr = crud.create_step(order=order, 
        instruction=instr_text, recipe_id=recipe_id)
    db.session.add(new_instr)
    db.session.commit()
    
    return new_instr.instruction

@app.route('/search')
def search():
    given_cuisine = request.args.get('cuisine')
    results = crud.get_recipes_by_cuisine(given_cuisine)
    print(results, "\n")
    return render_template("recipes.html", recipes=results)

@app.route('/add_fav')
def add_fav():
    user_id = session['current_user']
    recipe_id = request.args.get('recipe_id')        
    title = request.args.get('title')
    new_fav = crud.create_favorite(recipe_id, user_id)
    db.session.add(new_fav)
    db.session.commit()
    flash(f'{title} is saved into your Favorite recipes!')
    return new_fav

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
