let index=0
const recipe_id=document.querySelector('form').id

function instructionField() {
    const button1=document.querySelector(`#instrBttn${index}`);
    button1.addEventListener('click', (evt) => {
        evt.preventDefault();
        const formInputs={
            recipe_id: document.querySelector('#hidden_input').value,
            instructionText: document.querySelector(`#newInstr${index}`).value,
            order: index,
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
};
instructionField();

const button2=document.querySelector('.addStep');
button2.addEventListener('click', (evt) => {
    evt.preventDefault();
    index+=1;
    document.querySelector('#steps').insertAdjacentHTML('beforeend', 
        ` <li>Instructions <input id="newInstr${index}"`+
        `type="text" name="step" size=300><button id="instrBttn${index}" type="submit"> add </button></li>`);

    instructionField();
    });
