const editEmailBttn=document.querySelector('#editEmail');
editEmailBttn.addEventListener('click', (evt) => {
        evt.preventDefault();        
        document.getElementById("#newEmailForm").hidden='false'
});
const saveNewEmailBttn=document.querySelector('#saveNewEmail');
saveNewEmailBttn.addEventListener('click', (evt) => {
        evt.preventDefault();
        const emailFormInputs={
            newEmail: document.querySelector('#newEmail').value
        };
        console.log(emailFormInputs)
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
let prefIndex=0

function addPref(evt){
    evt.preventDefault();
    prefIndex+=1
    document.querySelector('#user_preferences').insertAdjacentHTML('beforeend', 
    `<p><input type="text" name="pref"> cuisine/diet`+
    `<button class="addPref" id="addPref${prefIndex}">`+
    `Do you want to add another interest?</button></p>`);
    document.querySelector(`#addPref${prefIndex}`).addEventListener('click', (evt) => {
        addPref(evt);
    });
};


function preferenceField(){
    const newPrefBttn=document.querySelector(`#addPref${prefIndex}`);
    newPrefBttn.addEventListener('click', (evt) => {
        addPref(evt);
    });
};
preferenceField()


// const saveChangesBttn = document.querySelector('#saveChangesBttn');
// saveChangesBttn.addEventListener('click',() => {
//     let preferences = [];
//     const num_preferences = document.querySelectorAll('.addPref').length
//     for (let i = 0; i <= num_preferences; i += 1){
//         preferences.push(document.querySelector(`#newPref${i}`).value)       
//     }
//     fetch('/add_preferences',{
//         method: 'POST',
//         body: JSON.stringify(preferences),
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     })
//     .then(response => response.json())
//     .then (responseData => {
//         document.querySelector('#user_preferences').innerText = responseData;
//     })
// });