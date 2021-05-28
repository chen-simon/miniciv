const canvas = document.getElementById('canvas');
const messageBox = document.getElementById('message');
const ctx = canvas.getContext('2d');

let timeOfLastFrame = new Date();
let currentInputs = {'up': false, 'left': false, 'down': false, 'right': false};
let updateLastFrame = true;

const renderGame = (screen) => {
    for (let y = 0; y < 48; y++) {
        for (let x = 0; x < 120; x++) {
            ctx.fillStyle = screen[y][x];
            ctx.fillRect(x * 16, y * 16, 16, 16);
        }
    }
};

const getInputs = (evt) => {
    if (evt.keyCode === 37) { currentInputs.left = true; }
    else if (evt.keyCode === 38) { currentInputs.up = true; }
    else if (evt.keyCode === 39) { currentInputs.right = true; }
    else if (evt.keyCode === 40) { currentInputs.down = true; }
    console.log(evt.keyCode)
};

const resetInputs = () => {
    currentInputs = {'up': false, 'left': false, 'down': false, 'right': false};
};

// Where inputs are in the JSON form {'up': False, 
//                                    'left': False, 
//                                    'down': False,
//                                    'right': True }
const updateGame = async () => {
    const inputsToSend = currentInputs;
    resetInputs();
    const response = await fetch('/game/', {method: 'POST', body: JSON.stringify(inputsToSend)});
    const data = await response.json();
    
    renderGame(data.screen);

    const currentTime = new Date();
    let deltaTime = currentTime - timeOfLastFrame;
    timeOfLastFrame = currentTime;

    messageBox.innerHTML = `FPS: ${1000 / deltaTime}`;
    updateLastFrame = true;
};


document.addEventListener('keydown', getInputs);

window.setInterval(() => {
    if (updateLastFrame) { 
        updateLastFrame = false;
        updateGame();
    }
}, 83.34);