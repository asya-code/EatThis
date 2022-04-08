const favBttn=document.querySelector('#add_fav');
favBttn.addEventListener('click', (evt) => {
    // evt.preventDefault();
    const favData = {
        favRecipeId: document.querySelector('#hidden_recipe_id').value,
        favRecipeTitle: document.querySelector('#hidden_recipe_title').value,
    };
    fetch('/add_fav', {
        method: 'POST',
        body: JSON.stringify(favData),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    document.querySelector('#add_fav').remove()
    document.querySelector('#new_rating').innerHTML = String(Number(document.querySelector('#new_rating').innerHTML) + 1) 
});