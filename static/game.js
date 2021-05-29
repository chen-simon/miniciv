const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Info boxes
const titleBox = document.getElementById('title');
const messageBox = document.getElementById('message');
const controlsBox = document.getElementById('controls');
const listBox = document.getElementById('list');
const textBox = document.getElementById('text-box');

// Game details
let updateLastFrame = true;
let isUsersTurn = true;

// Misc
const validKeys =  ['Space', 'ArrowUp', 'ArrowLeft', 'ArrowRight', 'ArrowDown', 'Tab', 'Enter', 'Escape'];

// Functions
const renderGame = (screen) => {
    for (let y = 0; y < 48; y++) {
        for (let x = 0; x < 120; x++) {
            ctx.fillStyle = screen[y][x];
            ctx.fillRect(x * 16, y * 16, 16, 16);
        }
    }
};

const updateInfo = ({title, message, list, controls}) => {
    if (title) { titleBox.innerHTML = title; }
    if (message) { messageBox.innerHTML = message; }
    if (controls) { controlsBox.innerHTML = controls; }
    if (list) { listBox.innerHTML = list; }
};

const getInputs = (evt) => {
    if (updateLastFrame && isUsersTurn && validKeys.includes(evt.code)) { 
        updateGame({'key': evt.code}); 
    }
};

const updateGame = async (obj) => {
    updateLastFrame = false;
    // Async stuff
    const response = await fetch('/game/io/', {method: 'POST', body: JSON.stringify(obj)});
    const data = await response.json();

    
    renderGame(data.screen);
    updateInfo(data);
    
    // Game rendered
    updateLastFrame = true;
};


document.addEventListener('keydown', getInputs);

// Wait for the game to initialize before asking for data
window.setTimeout(
    updateGame({}), 1000
);