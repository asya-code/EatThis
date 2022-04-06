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
function preferenceField(){
    const newPrefBttn=document.querySelector('.addPref');
    newPrefBttn.addEventListener('click', (evt) => {
            evt.preventDefault();
            prefIndex+=1
            document.querySelector('#user_preferences').insertAdjacentHTML('beforeend', 
            `<p><input type="text" name="pref"> cuisine/diet`+
            `<button class="addPref" id="addPref${prefIndex}">`+
            `Do you want to add another interest?</button></p>`);
    });
};
preferenceField()
// const saveChangesBttn=document.querySelector('#saveChangesBttn');
//         let changesInputs={
//             newEmail: document.querySelector('#newPref${prefIndex}').value
//         };
//         fetch('/save_changes',{
//             method: 'POST',
//             body: JSON.stringify(emailFormInputs),
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//         })
//         .then(response => response.json())
//         .then (responseData => {
//             document.querySelector('#userEmail').innerText = responseData;
//         });
