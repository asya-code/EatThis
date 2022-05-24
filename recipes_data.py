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
cuisines = ["indonesian", "turkish", "thai", "moroccan", "japanese"]
diets = ["vegetarian", "carnivor", "keto", "bla"]
meals = ["breakfast", "lunch", "dinner", "supper", "appetizer", "supper", "party", "snack"]

# Create 10 users;
user_1 = crud.create_user(email = "skachkova.asya@gmail.com", password="test", username="Asya")
model.db.session.add(user_1)
model.db.session.commit()

for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"
    username = f"name{n}"
    user = crud.create_user(email, password, username)    
    model.db.session.add(user)
model.db.session.add(user)
model.db.session.commit()

# Get users ids:
users = crud.get_users()
users_id = []
for user in users:
    users_id.append(user.user_id)

# Real recipes
new_recipe_1 = crud.create_recipe(title="Salted-Butter Cookies", meal="breakfast", cuisine="american", added_by=None, diet=None, created_at=date.today())
model.db.session.add(new_recipe_1)
model.db.session.commit()    
image_11 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650243998/Chocolate-Chip-Cookies-I-Didn_t-Like-My-Family-Cookie-Recipe-So-I-Improved-It-13032018_eu60ql.jpg",recipe_id=1)
model.db.session.add(image_11)

new_recipe_2 = crud.create_recipe(title="Classic Easy Banana Bread", meal="lunch", cuisine="american", added_by=None, diet=None, created_at=date.today())
model.db.session.add(new_recipe_2)
model.db.session.commit()    
image_21 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650244138/EP-20150323-BananaBread-nochocolate-hires_mxunym.jpg",recipe_id=2)
model.db.session.add(image_21)


new_recipe_3 = crud.create_recipe(title="Chilli con carne recipe", meal="dinner", cuisine="mexican", added_by=None, diet=None, created_at=date.today())
model.db.session.add(new_recipe_3)
model.db.session.commit()    
image_31 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650244569/recipe-image-legacy-id-1001451_6-c8d72b8_ngwpol.webp",recipe_id=3)
model.db.session.add(image_31)



new_recipe_4 = crud.create_recipe(title="Spaghetti Bolognese", meal="dinner", cuisine="Italian", added_by=None, diet=None, created_at=date.today())
model.db.session.add(new_recipe_4)
model.db.session.commit()    
image_41 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650244382/the-best-spaghetti-bolognese-7e83155_ibw6df.webp",recipe_id=4)
model.db.session.add(image_41)



new_recipe_5 = crud.create_recipe(title="Roast Potatoes", meal="lunch", cuisine="american", added_by=None, diet=None, created_at=date.today())
model.db.session.add(new_recipe_5)
model.db.session.commit()    
image_51 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650244466/roast-potatoes-main-7b0e23a_vc3utg.webp",recipe_id=5)
model.db.session.add(image_51)

new_recipe_6 = crud.create_recipe(title="Toad-in-the-hole", meal="dessert", cuisine="international", added_by=None, diet=None, created_at=date.today())
model.db.session.add(new_recipe_6)
model.db.session.commit()    
image_61 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650246173/toad-in-the-hole-delish-1639407751_sflhjm.png",recipe_id=6)
model.db.session.add(image_61)
image_62 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650246279/image_gnlkkk.jpg",recipe_id=6)
model.db.session.add(image_62)
image_63 = crud.create_image(url="https://res.cloudinary.com/eat-this/image/upload/v1650244718/recipe-image-legacy-id-736458_11-5ff6be2_cckmr9.webp",recipe_id=6)
model.db.session.add(image_63)
ingredient_1 = crud.create_ingredient(ing_name="chipolatas", qty=12, recipe_id=6, unit="pieces")
model.db.session.add(ingredient_1)
ingredient_2 = crud.create_ingredient(ing_name="sunflower oil", qty=1, recipe_id=6, unit="tbsp")
model.db.session.add(ingredient_2)
ingredient_3 = crud.create_ingredient(ing_name="flour", qty=120, recipe_id=6, unit="gramm")
model.db.session.add(ingredient_3)
ingredient_4 = crud.create_ingredient(ing_name="eggs", qty=2, recipe_id=6, unit=" ")
model.db.session.add(ingredient_4)
ingredient_5 = crud.create_ingredient(ing_name="semi-skimmed milk", qty=175, recipe_id=6, unit="ml")
model.db.session.add(ingredient_5)
step_1 = crud.create_step(instruction="Heat the oven to 220C/200C fan/gas 7. Put the chipolatas in a 20 x 30cm roasting tin with the oil and bake for 15 mins until browned.", recipe_id=6, order=0)
model.db.session.add(step_1)
step_2 = crud.create_step(instruction="Meanwhile, make the batter. Tip the flour into a bowl with ½ tsp salt, make a well in the middle and crack the eggs into it. Use an electric whisk to mix it together, then slowly add the milk, whisking all the time. Leave to stand until the sausages are nice and brown.", recipe_id=6, order=1)
model.db.session.add(step_2)
step_3 = crud.create_step(instruction="Remove the sausages from the oven – be careful because the fat will be sizzling hot – but if it isn’t, put the tin on the hob for a few minutes until it is.", recipe_id=6, order=2)
model.db.session.add(step_3)
step_4 = crud.create_step(instruction="Pour in the batter mix, transfer to the top shelf of the oven, then cook for 25-30 mins, until risen and golden. Serve with gravy and your favourite veg.", recipe_id=6, order=3)
model.db.session.add(step_4)



model.db.session.commit()

# Create favorites
for n in range(1,6):
    favorite_1 = crud.create_favorite(recipe_id=6, user_id=choice(users_id))
    model.db.session.add(favorite_1)
    favorite = crud.create_favorite(recipe_id=n, user_id=choice(users_id))
    model.db.session.add(favorite)
model.db.session.commit()

# # Create 10 recipes:
# for n in range(10):
#     new_recipe = crud.create_recipe(title=choice(titles), 
#         cuisine=choice(cuisines), added_by=choice(users_id), diet=choice(diets), meal=choice(meals))
#     model.db.session.add(new_recipe)
# model.db.session.commit()    


# new_recipe_2 = crud.create_recipe(title, meal=None, cuisine=None, added_by=None, diet=None, created_at=date.today())
# model.db.session.add(new_recipe_2)
# new_recipe_1 = crud.create_recipe(title, meal=None, cuisine=None, added_by=None, diet=None, created_at=date.today())
# model.db.session.add(new_recipe_1)
# model.db.session.commit()    

# Get recipes ids:
# recipes = crud.get_recipes()
# recipes_id = []
# num = 1

# img_list = ["https://res.cloudinary.com/eat-this/image/upload/v1648600814/10_umfvpo.jpg", 
# "https://res.cloudinary.com/eat-this/image/upload/v1648600814/6_ftjl5n.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600814/9_qxvkvw.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600813/2_gmpw3t.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600814/7_xbkshw.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600813/3_sbfeup.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600813/5_pzq4gz.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600813/1_aifxcw.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648600813/0_yhhm5i.jpg",
# "https://res.cloudinary.com/eat-this/image/upload/v1648574705/slow-roasted-butter-eggplant-curry-152139-2_qogtdm.jpg"]


# for cur_recipe in recipes:
#     recipes_id.append(cur_recipe.recipe_id)
    # Assotiate images to recipes:
    # image_1 = crud.create_image(url=f"{choice(img_list)}",recipe_id=cur_recipe.recipe_id)
    # image_2 = crud.create_image(url=f"{choice(img_list)}",recipe_id=cur_recipe.recipe_id)
    # model.db.session.add(image_1)
    # model.db.session.add(image_2)
#     num += 1
#     for n in range(randint(3, 6)):
#         ingredient = crud.create_ingredient(ing_name=choice(ingredients), qty=randint(1, 10), recipe_id=(cur_recipe.recipe_id), unit=choice(units))
#         model.db.session.add(ingredient)
#     for n in range(randint(1, 3)):
#         step = crud.create_step(instruction=choice(steps), recipe_id=cur_recipe.recipe_id,order=n+1)
#         model.db.session.add(step)

# for n in range(5):
#     favorite = crud.create_favorite(recipe_id=choice(recipes_id), user_id=choice(users_id))
#     model.db.session.add(favorite)

# for n in range (10):
#     preference = crud.create_preference(user_id=choice(users_id), interest=choice(cuisines+diets))
#     model.db.session.add(preference)

# model.db.session.commit()
