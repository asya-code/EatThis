"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime, date

import crud
import model
import server

os.system("dropdb eat_this")
os.system("createdb eat_this")

model.connect_to_db(server.app)
model.db.create_all()

ingredients = ["sea", "sky", "water", "flower", "tiger", "phone"]
units = ["cup", "gram", "handfull", "bucket"]
steps = ["boil water", "add salt", "enjoy!"]
titles = ["Food Enchiladas", "Beer Kielbasa", "Coconut Shrimp",
    "Crab Remoulade", "Favorite soup", "Frito nose", 
    "General' Tso", "Greek Gyros"]
cuisines = ["Indonesian", "Turkish", "Thai", "Moroccan", "Japanese"]

# Create 10 users;
for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"
    username = f"name{n}"
    user = crud.create_user(email, password, username)    
    model.db.session.add(user)
model.db.session.commit()

# Get users ids:
users = crud.get_users()
users_id = []
for user in users:
    users_id.append(user.user_id)

# Create 10 recipes:
for n in range(10):
    new_recipe = crud.create_recipe(title=choice(titles), 
        cuisine=choice(cuisines), added_by=choice(users_id), )
    model.db.session.add(new_recipe)
model.db.session.commit()    

# Get recipes ids:
recipes = crud.get_recipes()
recipes_id = []
num = 1
img_list = ["https://res.cloudinary.com/eat-this/image/upload/v1648574705/Vanilla-cinnamon-breakfast-rice-bowls-c9757f6_l8iuk3.webp", "https://res.cloudinary.com/eat-this/image/upload/v1648574705/slow-roasted-butter-eggplant-curry-152139-2_qogtdm.jpg", "https://res.cloudinary.com/eat-this/image/upload/v1648574705/spanakopita-765dfd2_qnowgw.webp", "https://res.cloudinary.com/eat-this/image/upload/v1648574705/wild-garlic-nettle-soup-23d5de8_p77jsi.webp", "https://res.cloudinary.com/eat-this/image/upload/v1648574705/Vegan-tomato-spinach-quiche-93aba36_cr7rta.webp", "https://res.cloudinary.com/eat-this/image/upload/v1648574705/easy-butter-chicken-7d9efe3_rmbbcu.webp", "https://res.cloudinary.com/eat-this/image/upload/v1648574705/meatball-black-bean-chilli-7cb50d5_s9dsqk.webp"]
for cur_recipe in recipes:
    recipes_id.append(cur_recipe.recipe_id)
    # Assotiate images to recipes:
    new_image = crud.create_image(url=f"{choice(img_list)}",recipe_id=cur_recipe.recipe_id)
    model.db.session.add(new_image)
    num += 1
    for n in range(randint(3, 6)):
        ingredient = crud.create_ingredient(ing_name=choice(ingredients), qty=randint(1, 10), recipe_id=(cur_recipe.recipe_id), unit=choice(units))
        model.db.session.add(ingredient)
    for n in range(randint(1, 3)):
        step = crud.create_step(instruction=choice(steps), recipe_id=cur_recipe.recipe_id,order=n+1)
        model.db.session.add(step)

for n in range(5):
    favorite = crud.create_favorite(recipe_id=choice(recipes_id), user_id=choice(users_id))
    model.db.session.add(favorite)

model.db.session.commit()
