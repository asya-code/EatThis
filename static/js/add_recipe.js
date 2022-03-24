let index=0
const recipe_id=document.querySelector('form').id

const button1=document.querySelector('.addInstr');
button1.addEventListener('click', (evt) => {
    evt.preventDefault();
    const formInputs={
        recipe_id: document.querySelector('form').id,
        instructionText: document.querySelector(`#newInstr${evt.target.id}`).value,
        order: document.querySelector(`#newInstr${evt.target.id}`).value,
    };
    fetch('/add_instr',{
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then (responseData => {
        document.querySelector('.newInstr').innerText = responseData;
    });
});

const button2=document.querySelector('.addStep');
button2.addEventListener('click', (evt) => {
    evt.preventDefault();
    index+=1;
    document.querySelector('#steps').insertAdjacentHTML('beforeend', 
        ` <li>Instructions <input id="newInstr${index}"`+
        `type="text" name="step" size=300><button class='addInstr' id="${index}" type="submit"> add </button></li>`);

    });

const button3=document.querySelector('#instrDone');
button2.addEventListener('click', () => {
    
})

