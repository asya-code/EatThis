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
    .then (document.querySelector('#add_fav').remove())
    // .then (response => response.text())
    // .then (responseText => {
    //     alert(responseText);
    // });
    // document.querySelector('#add_fav').disabled = true;

});