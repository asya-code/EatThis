let stepIndex=0
let ingIndex=0
let qtyIndex=0
let unitIndex=0

const recipe_id=document.querySelector('form').id

function ingredientField() {
    const ingrBttn=document.querySelector(`#ingrBttn${ingIndex}`);
    ingrBttn.addEventListener('click', (evt) => {
        evt.preventDefault();
        const ingInputs={
            recipe_id: document.querySelector('#hidden_input').value,
            ingredientText: document.querySelector(`#newIngr${ingIndex}`).value,
            qty: document.querySelector(`#newQty${qtyIndex}`).value,
            unit: document.querySelector(`#newUnit${unitIndex}`).value,
        };
        fetch('/add_ingredient',{
            method: 'POST',
            body: JSON.stringify(ingInputs),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then (responseData => {
            document.querySelector('.newIngr').innerText = responseData;
        });
    });
};
ingredientField();

const nextIngrBttn=document.querySelector('.nextIngr');
nextIngrBttn.addEventListener('click', (evt) => {
    evt.preventDefault();
    ingIndex+=1;
    document.querySelector('#ingredients').insertAdjacentHTML('beforeend', 
        ` <li> Ingredient <input id="newIngr${ingIndex}"`+
        `type="text" name="ingredient" size=300><input class="newQty" id="newQty${qtyIndex}" type="number" name="qty">
        <label for="unit"> units </label>
        <select name="unit" id="newUnit${unitIndex}">
            <option value="gram"> gram </option>
            <option value="oz"> oz </option>
            <option value="ml"> ml </option>
            <option value="fl oz"> fl oz </option>
            <option value="cup"> cup </option>
        </select><button id="ingrBttn${ingIndex}" type="submit"> add </button></li>`);

    ingredientField();
    });














function instructionField() {
    const instrBttn=document.querySelector(`#instrBttn${stepIndex}`);
    instrBttn.addEventListener('click', (evt) => {
        evt.preventDefault();
        const formInputs={
            recipe_id: document.querySelector('#hidden_input').value,
            instructionText: document.querySelector(`#newInstr${stepIndex}`).value,
            order: stepIndex,
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

const addStepBttn=document.querySelector('.addStep');
addStepBttn.addEventListener('click', (evt) => {
    evt.preventDefault();
    stepIndex+=1;
    document.querySelector('#steps').insertAdjacentHTML('beforeend', 
        ` <li>Instructions <input id="newInstr${stepIndex}"`+
        `type="text" name="step" size=300><button id="instrBttn${stepIndex}" type="submit"> add </button></li>`);

    instructionField();
    });
