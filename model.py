from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


db = SQLAlchemy()

class User(db.Model):
    """A user."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    full_name = db.Column(db.String(75))
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=date.today())
    user_image = db.Column(db.String)
    # user.recipes 
    # user.favorites
    def __repr__(self):
        return f"<User user_id={self.user_id}, email={self.email}, username={self.username}>"

class Recipe(db.Model):
    """A recipe."""
    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(25))
    created_at = db.Column(db.DateTime, nullable=False, default=date.today())
    added_by = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    diet = db.Column(db.String)
    meal = db.Column(db.String) # meal type (breakf, lunch etc)
    #recipe.steps
    #recipe.favorites
    #recipes.ingredients
    #recipe.images

    user = db.relationship("User", backref="recipes")

    def __repr__(self):
        return f"<Recipe recipe_id={self.recipe_id}, title={self.title}, added_by={self.added_by}>"

class Step(db.Model):
    """Recipe preparation steps."""
    __tablename__ = "steps"

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    instruction = db.Column(db.Text, nullable=False)
    step_image = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    order = db.Column(db.Integer, nullable=False)

    recipe = db.relationship("Recipe", backref="steps")

    def __repr__(self):
        return f"<Step step_id={self.step_id}, recipe={self.recipe_id}>"

class Favorite(db.Model):
    """Recipes added to favorites by particular user."""
    __tablename__ = "favorites"

    fav_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    recipe = db.relationship("Recipe", backref="favorites")
    user = db.relationship("User", backref="favorites")

    def __repr__(self):
        return f"<Favorite recipe_id={self.recipe_id}, chosen by user_id={self.user_id}>"

class Ingredient(db.Model):
    __tablename__ = "ingredients"

    ing_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ing_name = db.Column(db.String(100), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    unit = db.Column(db.String, nullable=False, default="gram")

    recipe = db.relationship("Recipe", backref="ingredients")
    
    def __repr__(self):
        return f"<Ingredient ing_id={self.ing_id}, ing_name={self.ing_name}, recipe_id={self.recipe_id}>"

class Image(db.Model):
    __tablename__ = "images"

    img_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String)
#    step_id = db.Column(db.Integer, db.ForeignKey("step.") nullable=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=True)

#    step = db.relashionship("Step", backref="images")
    recipe = db.relationship("Recipe", backref="images")

    def __repr__(self):
        return f"<Image img_id={self.img_id}, recipe_id={self.recipe_id}>"

def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app, "eat_this")
