const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');


const renderGame = (screen) => {
    for (let y = 0; y < 3; y++) {
        for (let x = 0; x < 3; x++) {
            ctx.fillStyle = screen[y][x];
            ctx.fillRect(x * 16, y * 16, 16, 16);
        }
    }
};

const updateGame = async () => {
    const response = await fetch('/debug/tile/', {method: 'GET'});
    const data = await response.json();

    console.log(data)
    
    renderGame(data.screen);
};

updateGame();