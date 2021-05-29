
const startGame = async () => {
    alert("EEE")
    const hi = await fetch('/start/', {method: 'POST', body: JSON.stringify({'name': 'simon'})});
    console.log(letssee);
};