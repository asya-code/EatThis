const editEmailBttn=document.querySelector('#editEmail');
editEmailBttn.addEventListener('click', (evt) => {
        evt.preventDefault();
        console.log("new block")
        document.querySelector('#userEmail').insertAdjacentHTML('beforeend', 
        '<form id=newEmail action="/change_email" method="post">'+
        '<p> New email <input id="newEmail"'+
        'type="text" name="email"><button id="=saveNewEmail" type="submit"> save </button></p>'+
        '</form>');
});
const saveNewEmailBttn=document.querySelector('#saveNewEmail');
saveNewEmailBttn.addEventListener('click', (evt) => {
        evt.preventDefault();
        const emailFormInputs={
            new_email: document.querySelector('#newEmail').value
        };
        fetch('/change_email',{
            method: 'POST',
            body: JSON.stringify(emailFormInputs),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then (responseData => {
            document.querySelector('#userEmail').innerText = responseData;
        });
    });
const prefIndex=0
function preferenceField(){
    while (prefIndex < 5) {
    const addPrefFieldBttn=document.querySelector(`#addPref${prefIndex}`);
    addPrefFieldBttn.addEventListener('click', (evt) => {
            evt.preventDefault();
            document.querySelector(`#newPref${prefIndex-1}`).insertAdjacentHTML('beforeend', 
            `<select name="cuisine" id="newPref${prefIndex}">`+
            `<option value="indonesian"> indonesian </option>`+
            `<option value="turkish"> turkish </option>`+
            `<option value="thai"> thai </option>`+
            `<option value="moroccan"> moroccan </option>`+
            '<option value="japanese"> japanese </option></select>'+
        `<label for="cuisine"> cuisine *</label>`+
        `<button id="addPref${prefIndex}"> Do you want to add another interest? </button>`);
            prefIndex+=1
    })
}};