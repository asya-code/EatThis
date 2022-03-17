from model import db, User, Recipe, Step, Favorite, Ingredient, Image, connect_to_db
from datetime import datetime, date

def create_user(email, password, username, full_name=None, created_at=date.today()):
    """Create and return a new user."""
    user = User(email=email, password=password, username=username)
    return user

def get_users():
    """Return all users."""
    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key."""
    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()



def create_recipe(title, cuisine=None, added_by=None, diet=None, created_at=date.today()):
    """Create and return a new recipe."""
    recipe = Recipe(
        title=title,
        cuisine=cuisine,
        created_at=created_at,
        added_by=added_by,
        diet=diet)
    return recipe

def get_recipes():
    """Return all recipes."""
    return Recipe.query.all()

def get_recipe_by_id(recipe_id):
    """Return a recipe by primary key."""
    return Recipe.query.get(recipe_id)

def get_recipes_by_added(user_id):
    """Return all recipes added by specific user""" 
    return Recipe.querry.filter(Recipe.added_by==user_id).all()

def get_recipes_by_cuisine(given_cuisine):
    """Return all recipes assosciated with particular cuisine"""
    return Recipe.querry.filter(Recipe.cuisine==given_cuisine).all()

def get_recipes_by_diet(given_diet):
    """Return all recipes assosciated with particular diet"""
    return Recipe.querry.filter(Recipe.diet==given_diet).all()

def get_recipes_by_meal(given_meal):
    """Return all recipes assosciated with 
        particular meal time (breakfast, lunch, dinner)"""
    return Recipe.querry.filter(Recipe.diet==given_meal).all()


def create_step(instruction, step_image, recipe_id, order):
    """Create and return a new cooking step for the recipe."""
    step = Step(
        instruction=instruction,
        step_image=step_image,
        recipe_id=recipe_id,
        order=order)
    return step


def get_steps():
    """Return all steps ."""
    return Step.query.all()

def get_step_by_id(step_id):
    """Return a step by primary key."""
    return Step.query.get(step_id)

def get_steps_by_recipe_id(given_recipe_id):
    """Return all steps for particulat recipe."""
    return Step.querry.filter(Step.recipe_id==given_recipe_id).all()



def create_favorite(recipe_id, user_id):
    """Create and return a new favorite object (user-recipe pair)."""
    favorite = Favorite(
        recipe_id=recipe_id,
        user_id=user_id)
    return favorite

def get_fav_by_id(fav_id):
    """Return a recipe by primary key."""
    return Favorite.query.get(fav_id)

def get_favorites():
    """Return all favorites."""
    return Favorite.query.all()

def get_favs_by_user_id(given_user_id):
    """Return all favorite recipes for particular user."""
    return Favorite.query.filter(Favorite.user_id==given_user_id).all()

def get_favs_by_recipe_id(given_recipe_id):
    """Return all users who has this particular recipe in favorites""" 
    return Favorite.query.filter(Favorite.recipe_id==given_recipe_id).all()



def create_ingredient(ing_name, qty,recipe_id, unit, image=None):
    """Create and return a new favorite object (user-recipe pair)."""
    ingredient = Ingredient(
        ing_name=ing_name,
        qty=qty,
        image=image,
        recipe_id=recipe_id,
        unit=unit)
    return ingredient

def get_ingredients(ing_id):
    """Return ingredient by primary key."""
    return Ingredient.query.get(ing_id)

def get_ingredients():
    """Return all ingredients."""
    return Ingredient.query.all()

def get_ings_by_recipe_id(given_recipe_id):
    """Return all ingredients for particular recipe."""
    return Ingredient.query.filter(Ingredient.recipe_id==given_recipe_id).all()

def get_ing_by_recipe_id(given_recipe_id):
    """Return all users who has this particular recipe in favorites""" 
    return Favorite.query.filter(Favorite.recipe_id==given_recipe_id).all()



def create_image(url, step_id,recipe_id):
    """Create and return a new image object."""
    image = Image(
        url=url,
        step_id=step_id,
        recipe_id=recipe_id)
    return image

def get_image_by_id(img_id):
    """Return image by primary key."""
    return Image.query.get(ing_id)

def get_images():
    """Return all images."""
    return Image.query.all()

def get_imgs_by_recipe_id(given_recipe_id):
    """Return all images for particular recipe."""
    return Image.query.filter(Image.recipe_id==given_recipe_id).all()

def get_imgs_by_step_id(given_step_id):
    """Return all images for particular step.""" 
    return Image.query.filter(Image.step_id==given_step_id).all()



if __name__ == "__main__":
    from server import app
    connect_to_db(app)