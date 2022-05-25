<h1 align="center">
  <a href="https://github.com/asya-code/EatThis.git">
    <!-- Please provide path to your logo here -->
    <div style="font-family: 'Shadows Into Light', cursive; font-size: x-large; color: Black">Eat This!</div>
  </a>
</h1>

<div align="center">
<br />

[![code with love by GITHUB_USERNAME](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-GITHUB_USERNAME-ff1414.svg?style=flat-square)](https://github.com/asya_code)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)


</details>

---

## About
<p>
EatThis - a smart recipe application which allows you to create, edit, favorite, and search for new recipes. This app has recommendation algorithms which consider the user's food preferences.
</p>

<details>
<br>

<img src="static/images/trending_today.png" title="Trending recipes" width="100%"> 
<br>
<img src="static/images/recommendations.png" title="Recommendations" width="100%">

</details>

### Built With

Backend is powered by Python with Flask web framework and SQLAlchemy as its ORM, PostgreSQL for database. The front-end is written in HTML, Jinja and Javascript. Bootstrap and css were used to style the app.

## Features
<p>
Unregistered guests can see the most popular recipes, browse all recipes and search particular ones by cuisine/diet/recipe name or ingredient.  After search button is pressed, request is send into my flask server which picks corresponding recipes from the database and sends them to the search results page.
<p>
<br>

<img src="static/images/search.png" title="Search results" width="100%">

<br>

Logged in users can add their own recipes with my “add new recipe” feature, that support multiple ingredients and instructions input and images attachment. Images are stored via Cloudinary API.  These recipes are private by default user can choose to publish it to the website too. On the backend Flasks creates a recipe and stores it in the database. 
<br>

<img src="static/images/add_new_recipe_typing.png" title="Add new recipe typing" width="100%">

<br>
When recipe was successfully submitted, user will be redirected to this recipe page immediately.
<br>
<img src="static/images/add_new_recipe_result.png" title="New recipe completed" width="100%">
<br>
Users also can add recipes to their favorites, I’ve used Javascript to implement this without reloading the page. Every favorite recipe can be modified according to user’s preferences, the amount of recipe variations is unlimited.
<br>
<img src="static/images/favorite_edit_button.png" title="Favorite recipe editing option" width="100%">

<br>
Another feature of my app is recipe recommendations based on user’s preferences.
<br>
<img src="static/images/Recommendations.png" title="Recommendations" width="100%">


## Getting Started

### Prerequisites

> **[?]**
> What are the project requirements/dependencies?

### Installation

> **[?]**
> Describe how to install and get started with the project.

## Usage

> **[?]**
> How does one go about using it?
> Provide various use cases and code examples here.

## Roadmap

Project starts on 03.14.2022, ends on Steps:

MVP
- Users can create a profile and log in
- Users can Store their own recipes - ingredients and steps, pictures (cloudinary API)
- Users can save favorite recipes

2.0
- Users can look for a new recipes by:
    Name
    Cousine
    Ingredients
- Recommendations available based on:
    Most used recipes
    Favorite cousine
    Trending

3.0
- Long term meal planning
- Meal Planning recommendations and suggestions
- Recipes recalculations according to a family/group size

Nice-to-haves
- Dietary adjustment to whole MPV
- Calories/nutritions calculator based recommendations

Main data will come from the static database, working on how to implement dynamic update of the database from online sources