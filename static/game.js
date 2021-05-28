const canvas = document.getElementById('canvas');
const messageBox = document.getElementById('message');
const ctx = canvas.getContext('2d');

let timeOfLastFrame = new Date();
let updateLastFrame = true;
let isUsersTurn = true;

const renderGame = (screen) => {
    for (let y = 0; y < 48; y++) {
        for (let x = 0; x < 120; x++) {
            ctx.fillStyle = screen[y][x];
            ctx.fillRect(x * 16, y * 16, 16, 16);
        }
    }
};

const getInputs = (evt) => {
    console.log(evt.key);

    updateGame({'key': evt.key});
};

const updateGame = async (object) => {
    const response = await fetch('/game/io/', {method: 'POST', body: JSON.stringify(object)});
    const data = await response.json();
    
    renderGame(data.screen);

    updateLastFrame = true;
};


document.addEventListener('keydown', getInputs);

updateGame();