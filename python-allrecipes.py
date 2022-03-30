from allrecipes import AllRecipes

# Search :
query_options = {
  "wt": "pork curry",         # Query keywords
  "ingIncl": "olives",        # 'Must be included' ingrdients (optional)
  "ingExcl": "onions salad",  # 'Must not be included' ingredients (optional)
  "sort": "re"                # Sorting options : 're' for relevance, 'ra' for rating, 'p' for popular (optional)
}
query_result = AllRecipes.search(query_options)

# Get :
main_recipe_url = query_result[0]['url']
detailed_recipe = AllRecipes.get(main_recipe_url)  # Get the details of the first returned recipe (most relevant in our case)

# Display result :
print("## %s :" % detailed_recipe['name'])  # Name of the recipe

for ingredient in detailed_recipe['ingredients']:  # List of ingredients
    print("- %s" % ingredient)

for step in detailed_recipe['steps']:  # List of cooking steps
    print("# %s" % step)